"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[6962,3539],{23539:(t,e,r)=>{r.r(e),r.d(e,{default:()=>m});var n=r(70714),a=r(62426),o=r(28804),i=r(66006),s=r(89180),c=r(74861);const l="HTML Viewer";var d;!function(t){t.trustHTML="htmlviewer:trust-html"}(d||(d={}));const u={activate:function(t,e,r,n,i,s){let m;const T=e.load("jupyterlab");s&&(s.registerFactory(l,"refresh",(t=>o.ToolbarItems.createRefreshButton(t,e))),s.registerFactory(l,"trust",(t=>o.ToolbarItems.createTrustButton(t,e))),i&&(m=(0,a.createToolbarFactory)(s,i,l,u.id,e)));const h={name:"html",contentType:"file",fileFormat:"text",displayName:T.__("HTML File"),extensions:[".html"],mimeTypes:["text/html"],icon:c.html5Icon};t.docRegistry.addFileType(h);const y=new o.HTMLViewerFactory({name:l,fileTypes:["html"],defaultFor:["html"],readOnly:!0,toolbarFactory:m,translator:e}),g=new a.WidgetTracker({namespace:"htmlviewer"});return n&&n.restore(g,{command:"docmanager:open",args:t=>({path:t.context.path,factory:"HTML Viewer"}),name:t=>t.context.path}),t.docRegistry.addWidgetFactory(y),y.widgetCreated.connect(((e,r)=>{var n,a;g.add(r),r.context.pathChanged.connect((()=>{g.save(r)})),r.trustedChanged.connect((()=>{t.commands.notifyCommandChanged(d.trustHTML)})),r.title.icon=h.icon,r.title.iconClass=null!==(n=h.iconClass)&&void 0!==n?n:"",r.title.iconLabel=null!==(a=h.iconLabel)&&void 0!==a?a:""})),t.commands.addCommand(d.trustHTML,{label:T.__("Trust HTML File"),caption:T.__("Whether the HTML file is trusted.\n    Trusting the file allows scripts to run in it,\n    which may result in security risks.\n    Only enable for files you trust."),isEnabled:()=>!!g.currentWidget,isToggled:()=>{const t=g.currentWidget;return!!t&&-1!==t.content.sandbox.indexOf("allow-scripts")},execute:()=>{const t=g.currentWidget;if(!t)return!1;t.trusted=!t.trusted}}),r&&r.addItem({command:d.trustHTML,category:T.__("File Operations")}),g},id:"@jupyterlab/htmlviewer-extension:plugin",provides:o.IHTMLViewerTracker,requires:[s.ITranslator],optional:[a.ICommandPalette,n.ILayoutRestorer,i.ISettingRegistry,a.IToolbarWidgetRegistry],autoStart:!0},m=u}}]);
//# sourceMappingURL=6962.db53086.js.map