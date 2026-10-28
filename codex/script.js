const copyButton = document.querySelector('#copy-prompt');
const promptText = document.querySelector('#starter-prompt');
const feedback = document.querySelector('#copy-feedback');

if (copyButton && promptText && feedback) {
  copyButton.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(promptText.textContent.trim());
      copyButton.querySelector('span:last-child').textContent = '已复制';
      feedback.textContent = '任务已复制。回到 Codex 粘贴并开始探索。';
      window.setTimeout(() => { copyButton.querySelector('span:last-child').textContent = '复制任务'; }, 2200);
    } catch {
      feedback.textContent = '浏览器暂不允许复制，请选中上方任务文字后手动复制。';
    }
  });
}
