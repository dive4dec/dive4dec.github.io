"use strict";
(self["webpackChunk_dive_jupyterlite_xeus_python_kernel"] = self["webpackChunk_dive_jupyterlite_xeus_python_kernel"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlite_server__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlite/server */ "webpack/sharing/consume/default/@jupyterlite/server/@jupyterlite/server");
/* harmony import */ var _jupyterlite_server__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlite_server__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlite_kernel__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlite/kernel */ "webpack/sharing/consume/default/@jupyterlite/kernel");
/* harmony import */ var _jupyterlite_kernel__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlite_kernel__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _xeus_server_kernel__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./xeus_server_kernel */ "./lib/xeus_server_kernel.js");
/* harmony import */ var _style_logos_python_logo_32x32_png__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../style/logos/python-logo-32x32.png */ "./style/logos/python-logo-32x32.png");
/* harmony import */ var _style_logos_python_logo_64x64_png__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../style/logos/python-logo-64x64.png */ "./style/logos/python-logo-64x64.png");
// Copyright (c) Thorsten Beier
// Copyright (c) JupyterLite Contributors
// Distributed under the terms of the Modified BSD License.





const server_kernel = {
    id: '@jupyterlite/xeus-python-kernel-extension:kernel',
    autoStart: true,
    requires: [_jupyterlite_kernel__WEBPACK_IMPORTED_MODULE_1__.IKernelSpecs, _jupyterlite_server__WEBPACK_IMPORTED_MODULE_0__.IServiceWorkerRegistrationWrapper],
    activate: (app, kernelspecs, serviceWorkerRegistrationWrapper) => {
        kernelspecs.register({
            spec: {
                name: 'xeus-python',
                display_name: 'Python (XPython)',
                language: 'python',
                argv: [],
                resources: {
                    'logo-32x32': _style_logos_python_logo_32x32_png__WEBPACK_IMPORTED_MODULE_2__["default"],
                    'logo-64x64': _style_logos_python_logo_64x64_png__WEBPACK_IMPORTED_MODULE_3__["default"]
                }
            },
            create: async (options) => {
                return new _xeus_server_kernel__WEBPACK_IMPORTED_MODULE_4__.XeusServerKernel({
                    ...options,
                    mountDrive: serviceWorkerRegistrationWrapper.enabled
                });
            }
        });
    }
};
const plugins = [server_kernel];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);


/***/ }),

/***/ "./lib/xeus_server_kernel.js":
/*!***********************************!*\
  !*** ./lib/xeus_server_kernel.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "XeusServerKernel": () => (/* binding */ XeusServerKernel)
/* harmony export */ });
/* harmony import */ var comlink__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! comlink */ "webpack/sharing/consume/default/comlink/comlink");
/* harmony import */ var comlink__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(comlink__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__);
// Copyright (c) Thorsten Beier
// Copyright (c) JupyterLite Contributors
// Distributed under the terms of the Modified BSD License.




class XeusServerKernel {
    /**
     * Instantiate a new XeusServerKernel
     *
     * @param options The instantiation options for a new XeusServerKernel
     */
    constructor(options) {
        this._isDisposed = false;
        this._disposed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__.Signal(this);
        this._executeDelegate = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__.PromiseDelegate();
        this._parentHeader = undefined;
        this._parent = undefined;
        const { id, name, sendMessage, location } = options;
        this._id = id;
        this._name = name;
        this._location = location;
        this._sendMessage = sendMessage;
        this._worker = new Worker(new URL(/* worker import */ __webpack_require__.p + __webpack_require__.u("lib_worker_js"), __webpack_require__.b), {
            type: undefined
        });
        this._worker.onmessage = e => {
            this._processWorkerMessage(e.data);
        };
        this._remote = (0,comlink__WEBPACK_IMPORTED_MODULE_0__.wrap)(this._worker);
        this.initFileSystem(options);
    }
    async handleMessage(msg) {
        this._parent = msg;
        this._parentHeader = msg.header;
        await this._sendMessageToWorker(msg);
    }
    async _sendMessageToWorker(msg) {
        // TODO Remove this??
        if (msg.header.msg_type !== 'input_reply') {
            this._executeDelegate = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__.PromiseDelegate();
        }
        await this._remote.processMessage({ msg, parent: this.parent });
        if (msg.header.msg_type !== 'input_reply') {
            return await this._executeDelegate.promise;
        }
    }
    /**
     * Get the last parent header
     */
    get parentHeader() {
        return this._parentHeader;
    }
    /**
     * Get the last parent message (mimick ipykernel's get_parent)
     */
    get parent() {
        return this._parent;
    }
    /**
     * Get the kernel location
     */
    get location() {
        return this._location;
    }
    /**
     * Process a message coming from the pyodide web worker.
     *
     * @param msg The worker message to process.
     */
    _processWorkerMessage(msg) {
        var _a, _b, _c, _d;
        if (!msg.header) {
            return;
        }
        msg.header.session = (_b = (_a = this._parentHeader) === null || _a === void 0 ? void 0 : _a.session) !== null && _b !== void 0 ? _b : '';
        msg.session = (_d = (_c = this._parentHeader) === null || _c === void 0 ? void 0 : _c.session) !== null && _d !== void 0 ? _d : '';
        this._sendMessage(msg);
        // resolve promise
        if (msg.header.msg_type === 'status' &&
            msg.content.execution_state === 'idle') {
            this._executeDelegate.resolve();
        }
    }
    /**
     * A promise that is fulfilled when the kernel is ready.
     */
    get ready() {
        return Promise.resolve();
    }
    /**
     * Return whether the kernel is disposed.
     */
    get isDisposed() {
        return this._isDisposed;
    }
    /**
     * A signal emitted when the kernel is disposed.
     */
    get disposed() {
        return this._disposed;
    }
    /**
     * Dispose the kernel.
     */
    dispose() {
        if (this.isDisposed) {
            return;
        }
        this._worker.terminate();
        this._worker = null;
        this._remote = null;
        this._isDisposed = true;
        this._disposed.emit(void 0);
    }
    /**
     * Get the kernel id
     */
    get id() {
        return this._id;
    }
    /**
     * Get the name of the kernel
     */
    get name() {
        return this._name;
    }
    async initFileSystem(options) {
        let driveName;
        let localPath;
        if (options.location.includes(':')) {
            const parts = options.location.split(':');
            driveName = parts[0];
            localPath = parts[1];
        }
        else {
            driveName = '';
            localPath = options.location;
        }
        await this._remote.ready();
        if (options.mountDrive) {
            await this._remote.mount(driveName, '/drive', _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__.PageConfig.getBaseUrl());
            await this._remote.cd(localPath);
        }
    }
}


/***/ }),

/***/ "./style/logos/python-logo-32x32.png":
/*!*******************************************!*\
  !*** ./style/logos/python-logo-32x32.png ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (__webpack_require__.p + "e32b5c282072d717887b60da73178fdd35a65dc3caeacba7a026e5a4255cc997.png");

/***/ }),

/***/ "./style/logos/python-logo-64x64.png":
/*!*******************************************!*\
  !*** ./style/logos/python-logo-64x64.png ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (__webpack_require__.p + "5c9063b436cedf0567480fe487ece0d1479ea9545f310cba93fa184ccbab290d.png");

/***/ })

}]);
//# sourceMappingURL=lib_index_js.31d9d7eba1ba490fac58.js.map