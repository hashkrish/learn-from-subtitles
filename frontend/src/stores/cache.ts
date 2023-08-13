import { writable } from 'svelte/store';

export let localCache = writable({});

export const clearLocalCache = () => {
	localCache.set({});
};
