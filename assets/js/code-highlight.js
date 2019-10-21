import hljs from 'highlight.js';

document.querySelectorAll('pre code').forEach(
  (block) => {
    hljs.highlightBlock(block);
  }
);
