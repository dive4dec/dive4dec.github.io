"use strict";(self.webpackChunk_deathbeds_ipydrawio_notebook=self.webpackChunk_deathbeds_ipydrawio_notebook||[]).push([[568],{568:(e,o,t)=>{t.r(o),t.d(o,{ALL_FORMATS:()=>i.t6,CMD_NS:()=>a.sr,CommandIds:()=>a.OF,IPYNB_DIO:()=>i.ET,IPYNB_PLAIN:()=>i.lN,NS:()=>a.NS,PACKAGE:()=>a.iR,PLUGIN_ID:()=>a.Uu,drawioIpynbIcon:()=>i.j5});var a=t(306),i=t(656)},656:(e,o,t)=>{t.d(o,{ET:()=>p,j5:()=>n,lN:()=>s,t6:()=>r});var a=t(972),i=t(886);const n=new(t(912).LabIcon)({name:"drawio:ipynb",svgstr:i.DRAWIO_ICON_SVG.replace(i.DRAWIO_ICON_CLASS_RE,"jp-icon-contrast3")}),s={ext:".ipynb",factoryName:`${i.JSON_FACTORY} (Notebook)`,key:"ipynb",format:"json",icon:n,label:"Notebook",mimetype:"application/x-ipynb+json",name:"dionotebook",pattern:"\\.*\\.ipynb$",contentType:"notebook",modelName:"notebook",isJson:!0,isEditable:!0,isExport:!0,isDefault:!1,isTransformed:!1,wantsModel:e=>"notebook"===e.type,save:e=>e,fromXML:(e,o)=>{const t=e.metadata.get(i.IPYDRAWIO_METADATA);e.metadata.set(i.IPYDRAWIO_METADATA,Object.assign(Object.assign({},t||{}),{xml:o}))},toXML:e=>{const o=e.metadata.get(i.IPYDRAWIO_METADATA);return(null==o?void 0:o.xml)?`${o.xml}`:""},exporter:async(e,o,t)=>{const n=e.adapter.toXML(),s=new a.NotebookModel;return s.metadata.set(i.IPYDRAWIO_METADATA,{xml:n}),s.toJSON()}},p=Object.assign(Object.assign({},s),{factoryName:`${i.JSON_FACTORY} (Diagram Notebook)`,key:"xmlipynb",ext:".dio.ipynb",name:"xmlipynb",isDefault:!0,pattern:".*\\.dio\\.ipynb$"}),r=[p,s]},306:(e,o,t)=>{t.d(o,{sr:()=>p,OF:()=>r,NS:()=>n,iR:()=>i,Uu:()=>s});const a=JSON.parse('{"name":"@deathbeds/ipydrawio-notebook","version":"1.2.1","bugs":{"url":"https://github.com/deathbeds/ipydrawio/issues"},"homepage":"https://ipydrawio.rtfd.io","dependencies":{"@jupyterlab/application":"^3.1.0","@jupyterlab/notebook":"^3.1.0","@deathbeds/ipydrawio":"^1.2.1"},"devDependencies":{"@jupyterlab/builder":"^3.4.0","typescript":"~4.2.3"},"files":["{lib,schema,style,src}/**/*.{ts,tsx,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,css}","LICENSE.txt"],"jupyterlab":{"extension":"lib/plugin.js","outputDir":"../../py_packages/ipydrawio/src/ipydrawio/ext/ipdnb","sharedPackages":{"@deathbeds/ipydrawio":{"bundled":false,"singleton":true}},"discovery":{"server":{"base":{"name":"ipydrawio"},"managers":["pip","conda"]}}},"main":"lib/index.js"}'),i=t.t(a,2),n=i.name,s=`${n}:plugin`,p="ipydrawio-notebook";var r;!function(e){e.open=`${p}:open`}(r||(r={}))}}]);