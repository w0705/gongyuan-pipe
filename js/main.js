// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
  // 示例：平滑滚动到锚点（未来扩展用）
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) target.scrollIntoView({ behavior: 'smooth' });
    });
  });

  // 可以在这里加入统计、动画等
  console.log('公元管道网站已就绪');
});