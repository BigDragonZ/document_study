const copyButtons = document.querySelectorAll('#copy-prompt, [data-copy-target]');

copyButtons.forEach((button) => {
  button.addEventListener('click', async () => {
    const targetId = button.id === 'copy-prompt' ? 'starter-prompt' : button.dataset.copyTarget;
    const target = document.getElementById(targetId);
    if (!target) return;

    const feedbackId = button.dataset.copyFeedback;
    const feedback = (feedbackId && document.getElementById(feedbackId)) ||
      button.parentElement.querySelector('.copy-status') || document.querySelector('#copy-feedback');
    const label = button.querySelector('[data-copy-label]') || button.querySelector('span:last-child');
    const originalLabel = label ? label.textContent : '';

    try {
      if (!navigator.clipboard || !window.isSecureContext) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(target.textContent.trim());
      if (label) label.textContent = '已复制';
      if (feedback) feedback.textContent = '内容已复制，可以粘贴到 Claude Code 或你的配置文件中。';
      window.clearTimeout(button.copyResetTimer);
      button.copyResetTimer = window.setTimeout(() => {
        if (label) label.textContent = originalLabel;
      }, 2200);
    } catch {
      if (feedback) feedback.textContent = '浏览器暂不允许自动复制，请选中内容后手动复制。';
    }
  });
});
