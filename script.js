function _addEvent(e,n,t){if("function"==typeof t)if(e.addEventListener)e.addEventListener(n,t,!1);else if(e.attachEvent)e.attachEvent("on"+n,t);else e["on"+n]}var _events=["ready"],_myLib=function(e){for(var n=0;n<_events.length;n++)this[_events[n]]=new function(e,n){this.add=function(t){_addEvent(e,n,t)}}(e,_events[n]).add},$gmx=function(e){return new _myLib(e)};!function(){function e(){var e=document.getElementsByTagName("meta");return"no plugins"===function(){for(var n=0;n<e.length;n++)if("gobmxhelper"===e[n].getAttribute("property"))return e[n].getAttribute("content")}()}function n(){t(e()?r:d)}function t(e){window.jQuery?Modernizr.load([{load:e}]):Modernizr.load([{load:"//ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js",complete:function(){window.jQuery||Modernizr.load(a+"jquery.min.js")}},{load:e}])}var a="https://framework-gb.cdn.gob.mx/",o=a+"assets/",i=o+"scripts/",r=[i+"main.js"],d=[i+"plugins.js",i+"main.js"];if(window.Modernizr)n();else{var s=document.createElement("script");s.type="text/javascript",s.src=i+"vendor/modernizr.js",document.getElementsByTagName("head")[0].appendChild(s);var c=document.createElement("script");c.type="text/javascript",c.src=i+"vendor/pace.min.js",document.getElementsByTagName("head")[0].appendChild(c),window.onload=function(){n()}}}();
