import { c as create_ssr_component, d as createEventDispatcher, e as escape, f as add_attribute, h as each, v as validate_component } from "../../chunks/index.js";
const Dropdown = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  createEventDispatcher();
  let { subtitleLanguage = "en" } = $$props;
  if ($$props.subtitleLanguage === void 0 && $$bindings.subtitleLanguage && subtitleLanguage !== void 0)
    $$bindings.subtitleLanguage(subtitleLanguage);
  return `<select class="m-4 rounded border p-2"><option value="en">English</option><option value="ja">Japanese</option></select>`;
});
const DragAndDrop_svelte_svelte_type_style_lang = "";
const css = {
  code: ".drop-area.svelte-6tqvla{border:2px dashed #ccc;padding:20px;text-align:center}.file-list.svelte-6tqvla{margin-top:10px}.drop-message.svelte-6tqvla{color:#999}#file-upload-button.svelte-6tqvla{color:transparent;background-color:transparent;border:none;outline:none;width:0}#file-upload-button-label.svelte-6tqvla{cursor:pointer}",
  map: null
};
const DragAndDrop = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  createEventDispatcher();
  let { subtitleLanguage = "en" } = $$props;
  if ($$props.subtitleLanguage === void 0 && $$bindings.subtitleLanguage && subtitleLanguage !== void 0)
    $$bindings.subtitleLanguage(subtitleLanguage);
  $$result.css.add(css);
  return `<div class="drop-area m-4 grid place-content-center p-1 svelte-6tqvla"><div class="file-list svelte-6tqvla"><div class="drop-message svelte-6tqvla">Drag and drop files here</div>
        <label id="file-upload-button-label" for="file-upload-button" class="text-blue-500 svelte-6tqvla"><span class="text-sm">or click to select files</span></label>
        <input id="file-upload-button" type="file" value="" class="svelte-6tqvla"></div>
</div>`;
});
const SubtitleHeader = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { title = "Sample subtitle heading" } = $$props;
  if ($$props.title === void 0 && $$bindings.title && title !== void 0)
    $$bindings.title(title);
  return `<div class="flex place-content-center p-1"><h1 class="text-xl">${escape(title)}</h1></div>`;
});
const Token = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { token = {} } = $$props;
  let { subtitleLanguage = "en" } = $$props;
  let japanese = subtitleLanguage === "ja" ? "text-xl" : "";
  if ($$props.token === void 0 && $$bindings.token && token !== void 0)
    $$bindings.token(token);
  if ($$props.subtitleLanguage === void 0 && $$bindings.subtitleLanguage && subtitleLanguage !== void 0)
    $$bindings.subtitleLanguage(subtitleLanguage);
  return `<span class="grid-columns-1 grid place-content-center">${subtitleLanguage === "ja" ? `<span>${token.pronounciation !== token.token ? `<span class="text-xs text-gray-500">${escape(token.pronounciation)}</span>` : `<span class="text-xs text-gray-500"> </span>`}</span>` : ``}
    <span${add_attribute("class", japanese, 0)}>${escape(token.token.replaceAll("（", "(").replaceAll("）", ")"))}</span></span>`;
});
function secondsToTimestamp(seconds) {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds - hours * 3600) / 60);
  const seconds_ = Math.floor(seconds - hours * 3600 - minutes * 60);
  const hours_str = hours < 10 ? "0" + hours : hours;
  const minutes_str = minutes < 10 ? "0" + minutes : minutes;
  const seconds_str = seconds_ < 10 ? "0" + seconds_ : seconds_;
  return `${hours_str}:${minutes_str}:${seconds_str}`;
}
const Subtitle = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { subtitle = {} } = $$props;
  let { subtitleLanguage = "en" } = $$props;
  if ($$props.subtitle === void 0 && $$bindings.subtitle && subtitle !== void 0)
    $$bindings.subtitle(subtitle);
  if ($$props.subtitleLanguage === void 0 && $$bindings.subtitleLanguage && subtitleLanguage !== void 0)
    $$bindings.subtitleLanguage(subtitleLanguage);
  return `<div class="m-1 border px-4 py-2"><span class="text-xs text-gray-500">${escape(secondsToTimestamp(subtitle.start))} - ${escape(secondsToTimestamp(subtitle.end))}</span>
    <div class="my-2 flex flex-wrap align-middle">${subtitle.content.length ? each(subtitle.content, (token) => {
    return `${validate_component(Token, "Token").$$render($$result, { token, subtitleLanguage }, {}, {})}`;
  }) : `<span>Upload a subtitle file to get started. </span>`}</div></div>`;
});
const SubtitleList = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { subtitles = [] } = $$props;
  let { subtitleLanguage = "en" } = $$props;
  if ($$props.subtitles === void 0 && $$bindings.subtitles && subtitles !== void 0)
    $$bindings.subtitles(subtitles);
  if ($$props.subtitleLanguage === void 0 && $$bindings.subtitleLanguage && subtitleLanguage !== void 0)
    $$bindings.subtitleLanguage(subtitleLanguage);
  return `<div class="flex place-content-center"><div class="m-4 grid p-2">${each(subtitles, (subtitle) => {
    return `${validate_component(Subtitle, "Subtitle").$$render($$result, { subtitle, subtitleLanguage }, {}, {})}`;
  })}</div></div>`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let title = "Sample Header";
  let subtitles = [];
  let subtitleLanguage = "en";
  return `<div class="m-2 flex place-content-center p-2"><h1 class="text-3xl">Learn from Subtitles</h1></div>


<span class="flex place-content-center">${validate_component(Dropdown, "Dropdown").$$render($$result, {}, {}, {})}
    
    </span>
${validate_component(DragAndDrop, "DragAndDrop").$$render($$result, {}, {}, {})}
${validate_component(SubtitleHeader, "SubtitleHeader").$$render($$result, { title }, {}, {})}
${validate_component(SubtitleList, "SubtitleList").$$render($$result, { subtitles, subtitleLanguage }, {}, {})}
`;
});
export {
  Page as default
};
