// Main JavaScript for Keshav Singh Portfolio

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                const offsetTop = targetSection.offsetTop - 80; // Account for fixed navbar
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                const navbarCollapse = document.querySelector('.navbar-collapse');
                if (navbarCollapse.classList.contains('show')) {
                    const navbarToggler = document.querySelector('.navbar-toggler');
                    navbarToggler.click();
                }
            }
        });
    });
    
    // Active navigation highlighting
    function updateActiveNav() {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
        
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            const sectionHeight = section.offsetHeight;
            
            if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    }
    
    // Update active nav on scroll
    window.addEventListener('scroll', updateActiveNav);
    
    // Navbar background on scroll
    function updateNavbarBackground() {
        const navbar = document.querySelector('.navbar');
        
        if (window.scrollY > 50) {
            navbar.style.backgroundColor = 'rgba(30, 41, 59, 0.98)';
        } else {
            navbar.style.backgroundColor = 'rgba(30, 41, 59, 0.95)';
        }
    }
    
    window.addEventListener('scroll', updateNavbarBackground);
    
    // Animate elements on scroll
    function animateOnScroll() {
        const elements = document.querySelectorAll('.card, .experience-item, .publication-item');
        
        elements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const elementVisible = 150;
            
            if (elementTop < window.innerHeight - elementVisible) {
                element.classList.add('fade-in-up');
            }
        });
    }
    
    window.addEventListener('scroll', animateOnScroll);
    
    // Initial call to animate elements already in view
    animateOnScroll();
    
    // Typing effect for hero section (optional enhancement)
    function typeWriter(element, text, speed = 100) {
        let i = 0;
        element.innerHTML = '';
        
        function type() {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        
        type();
    }
    
    // Add loading class to elements for animation
    const animatedElements = document.querySelectorAll('.card, .experience-item, .publication-item');
    animatedElements.forEach(element => {
        element.classList.add('loading');
    });
    
    // Remove loading class after a delay
    setTimeout(() => {
        animatedElements.forEach(element => {
            element.classList.remove('loading');
            element.classList.add('loaded');
        });
    }, 500);
    
    // Skill badges hover effect
    const skillBadges = document.querySelectorAll('.skills-list .badge');
    skillBadges.forEach(badge => {
        badge.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1) rotate(2deg)';
        });
        
        badge.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) rotate(0deg)';
        });
    });
    
    // Project cards tilt effect
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach(card => {
        card.addEventListener('mouseenter', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = (y - centerY) / 10;
            const rotateY = (centerX - x) / 10;
            
            this.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(10px)`;
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0px)';
        });
    });
    
    // Contact form validation (if you add a contact form later)
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
    
    // Scroll to top functionality
    function createScrollToTop() {
        const scrollButton = document.createElement('button');
        scrollButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
        scrollButton.className = 'scroll-to-top';
        scrollButton.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: linear-gradient(45deg, var(--primary-color), var(--accent-color));
            color: white;
            border: none;
            cursor: pointer;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            z-index: 1000;
            box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
        `;
        
        document.body.appendChild(scrollButton);
        
        scrollButton.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
        
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                scrollButton.style.opacity = '1';
                scrollButton.style.visibility = 'visible';
            } else {
                scrollButton.style.opacity = '0';
                scrollButton.style.visibility = 'hidden';
            }
        });
    }
    
    createScrollToTop();
    
    // Preloader (optional)
    function hidePreloader() {
        const preloader = document.querySelector('.preloader');
        if (preloader) {
            preloader.style.opacity = '0';
            setTimeout(() => {
                preloader.style.display = 'none';
            }, 500);
        }
    }
    
    // Hide preloader when page is loaded
    window.addEventListener('load', hidePreloader);
    
    // Performance optimization: Throttle scroll events
    function throttle(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    // Apply throttling to scroll events
    const throttledScroll = throttle(() => {
        updateActiveNav();
        updateNavbarBackground();
        animateOnScroll();
    }, 16); // ~60fps
    
    window.removeEventListener('scroll', updateActiveNav);
    window.removeEventListener('scroll', updateNavbarBackground);
    window.removeEventListener('scroll', animateOnScroll);
    window.addEventListener('scroll', throttledScroll);
    
    // Accessibility improvements
    document.addEventListener('keydown', function(e) {
        // Skip to main content with Tab key
        if (e.key === 'Tab' && !e.shiftKey) {
            const focusableElements = document.querySelectorAll(
                'a[href], button, textarea, input[type="text"], input[type="radio"], input[type="checkbox"], select'
            );
            
            // Add focus indicators
            focusableElements.forEach(element => {
                element.addEventListener('focus', function() {
                    this.style.outline = '2px solid var(--accent-color)';
                    this.style.outlineOffset = '2px';
                });
                
                element.addEventListener('blur', function() {
                    this.style.outline = 'none';
                });
            });
        }
    });
    
    // Console message for developers
    console.log(`
    🚀 Keshav Singh Portfolio Website
    
    Built with:
    - Flask (Python)
    - Bootstrap 5
    - Custom CSS & JavaScript
    
    Contact: to.keshav.singh@gmail.com
    GitHub: https://github.com/shaginhekvs
    `);
});

// Service Worker registration for PWA (optional future enhancement)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}
