import { init } from '../serverless.js';

export const handler = init({
	appDir: "_app",
	appPath: "_app",
	assets: new Set(["favicon.png","output.css"]),
	mimeTypes: {".png":"image/png",".css":"text/css"},
	_: {
		client: {"start":"_app/immutable/entry/start.cdf43cb8.js","app":"_app/immutable/entry/app.f2bb98b1.js","imports":["_app/immutable/entry/start.cdf43cb8.js","_app/immutable/chunks/index.568a4140.js","_app/immutable/chunks/singletons.cfcb0119.js","_app/immutable/entry/app.f2bb98b1.js","_app/immutable/chunks/index.568a4140.js"],"stylesheets":[],"fonts":[]},
		nodes: [
			() => import('../server/nodes/0.js'),
			() => import('../server/nodes/1.js'),
			() => import('../server/nodes/2.js')
		],
		routes: [
			{
				id: "/",
				pattern: /^\/$/,
				params: [],
				page: { layouts: [0,], errors: [1,], leaf: 2 },
				endpoint: null
			}
		],
		matchers: async () => {
			
			return {  };
		}
	}
});
