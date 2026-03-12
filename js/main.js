// 北京仝志伟业 - SMT 设备官网
// 主脚本文件

document.addEventListener('DOMContentLoaded', function() {
    console.log('仝志伟业官网加载完成');
    
    // 导航栏滚动效果
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.style.boxShadow = '0 2px 10px rgba(0,0,0,0.2)';
        } else {
            navbar.style.boxShadow = '0 2px 5px rgba(0,0,0,0.1)';
        }
    });
});
