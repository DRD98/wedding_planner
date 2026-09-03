/**
 * Wedding Planner - Digital Wedding Card & Invitation JS
 */

document.addEventListener('DOMContentLoaded', () => {
    initHeaderScroll();
    initCountdown();
    initMobileNavigation();
    initCalendarDropdown();
    initBackToTop();
    initSmoothScroll();
    initPasswordToggle();
});

/**
 * 1. Live Countdown Timer
 */
function initCountdown() {
    const countdownWrapper = document.getElementById('countdownWrapper');
    if (!countdownWrapper) return;

    const targetDateStr = countdownWrapper.getAttribute('data-target-date') || '2026-10-24T15:30:00';
    const targetDate = new Date(targetDateStr).getTime();

    const daysEl = document.getElementById('cdDays');
    const hoursEl = document.getElementById('cdHours');
    const minutesEl = document.getElementById('cdMinutes');
    const secondsEl = document.getElementById('cdSeconds');

    function updateCountdown() {
        const now = new Date().getTime();
        const difference = targetDate - now;

        if (difference <= 0) {
            if (daysEl) daysEl.textContent = '00';
            if (hoursEl) hoursEl.textContent = '00';
            if (minutesEl) minutesEl.textContent = '00';
            if (secondsEl) secondsEl.textContent = '00';
            const header = countdownWrapper.querySelector('.countdown-header');
            if (header) header.textContent = 'Happily Ever After!';
            return;
        }

        const days = Math.floor(difference / (1000 * 60 * 60 * 24));
        const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((difference % (1000 * 60)) / 1000);

        if (daysEl) daysEl.textContent = String(days).padStart(2, '0');
        if (hoursEl) hoursEl.textContent = String(hours).padStart(2, '0');
        if (minutesEl) minutesEl.textContent = String(minutes).padStart(2, '0');
        if (secondsEl) secondsEl.textContent = String(seconds).padStart(2, '0');
    }

    updateCountdown();
    setInterval(updateCountdown, 1000);
}

/**
 * 2. Mobile Navigation Drawer
 */
function initMobileNavigation() {
    const toggleBtn = document.getElementById('mobileToggle');
    const drawer = document.getElementById('mobileNavDrawer');
    if (!toggleBtn || !drawer) return;

    toggleBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isOpen = drawer.classList.contains('open');
        if (isOpen) {
            closeMobileNav();
        } else {
            openMobileNav();
        }
    });

    function openMobileNav() {
        drawer.classList.add('open');
        toggleBtn.classList.add('active');
        toggleBtn.setAttribute('aria-expanded', 'true');
        drawer.setAttribute('aria-hidden', 'false');
    }

    function closeMobileNav() {
        drawer.classList.remove('open');
        toggleBtn.classList.remove('active');
        toggleBtn.setAttribute('aria-expanded', 'false');
        drawer.setAttribute('aria-hidden', 'true');
    }

    // Close when clicking any mobile link
    const mobileLinks = drawer.querySelectorAll('.mobile-link');
    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            closeMobileNav();
        });
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
        if (!drawer.contains(e.target) && !toggleBtn.contains(e.target) && drawer.classList.contains('open')) {
            closeMobileNav();
        }
    });
}

/**
 * 3. Calendar Dropdown & Dynamic Links (.ics / Google / Outlook)
 */
function initCalendarDropdown() {
    const dropdown = document.querySelector('.calendar-dropdown');
    const btn = document.getElementById('calendarDropdownBtn');
    const googleLink = document.getElementById('googleCalLink');
    const icalLink = document.getElementById('icalDownloadLink');
    const outlookLink = document.getElementById('outlookCalLink');

    if (!dropdown || !btn) return;

    // Toggle dropdown
    btn.addEventListener('click', (e) => {
        e.stopPropagation();
        dropdown.classList.toggle('open');
        const isOpen = dropdown.classList.contains('open');
        btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
        if (!dropdown.contains(e.target)) {
            dropdown.classList.remove('open');
            btn.setAttribute('aria-expanded', 'false');
        }
    });

    // Event Information
    const eventDetails = {
        title: "Sophia & Liam's Wedding",
        description: "Join Sophia & Liam in celebrating their marriage at Villa Seraphina, Napa Valley.",
        location: "Villa Seraphina, 480 Vineyard Crest Road, Napa Valley, CA",
        // 2026-10-24 15:30 to 23:59 UTC format: 20261024T223000Z
        startISO: "20261024T223000Z",
        endISO: "20261025T070000Z",
        startDateFormatted: "20261024T153000",
        endDateFormatted: "20261025T000000"
    };

    // Google Calendar Link
    if (googleLink) {
        const googleUrl = `https://calendar.google.com/calendar/render?action=TEMPLATE&text=${encodeURIComponent(eventDetails.title)}&dates=${eventDetails.startISO}/${eventDetails.endISO}&details=${encodeURIComponent(eventDetails.description)}&location=${encodeURIComponent(eventDetails.location)}`;
        googleLink.href = googleUrl;
    }

    // Outlook Calendar Link
    if (outlookLink) {
        const outlookUrl = `https://outlook.live.com/calendar/0/deeplink/compose?subject=${encodeURIComponent(eventDetails.title)}&startdt=${eventDetails.startISO}&enddt=${eventDetails.endISO}&body=${encodeURIComponent(eventDetails.description)}&location=${encodeURIComponent(eventDetails.location)}`;
        outlookLink.href = outlookUrl;
    }

    // iCal (.ics) Dynamic Download
    if (icalLink) {
        icalLink.addEventListener('click', (e) => {
            e.preventDefault();
            const icsContent = [
                'BEGIN:VCALENDAR',
                'VERSION:2.0',
                'PRODID:-//Sophia and Liam//Wedding Invitation//EN',
                'CALSCALE:GREGORIAN',
                'METHOD:PUBLISH',
                'BEGIN:VEVENT',
                `SUMMARY:${eventDetails.title}`,
                `DESCRIPTION:${eventDetails.description}`,
                `LOCATION:${eventDetails.location}`,
                `DTSTART:${eventDetails.startISO}`,
                `DTEND:${eventDetails.endISO}`,
                'STATUS:CONFIRMED',
                'END:VEVENT',
                'END:VCALENDAR'
            ].join('\r\n');

            const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
            const link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.setAttribute('download', 'sophia-and-liam-wedding.ics');
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            dropdown.classList.remove('open');
        });
    }
}

/**
 * 4. Back to Top Button
 */
function initBackToTop() {
    const backToTopBtn = document.getElementById('backToTopBtn');
    if (!backToTopBtn) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 350) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }
    });

    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/**
 * 5. Smooth Scroll with Offset for Fixed Header
 */
function initSmoothScroll() {
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const targetId = link.getAttribute('href');
            if (targetId === '#' || !targetId) return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                const headerHeight = document.getElementById('siteHeader')?.offsetHeight || 70;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight - 15;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * 6. Header Scrolled State (Translucent to Frosted)
 */
function initHeaderScroll() {
    const siteHeader = document.getElementById('siteHeader');
    if (!siteHeader) return;

    function handleScroll() {
        if (window.scrollY > 60) {
            siteHeader.classList.add('scrolled');
        } else {
            siteHeader.classList.remove('scrolled');
        }
    }

    handleScroll();
    window.addEventListener('scroll', handleScroll, { passive: true });
}

/**
 * 7. Password Visibility Toggle
 */
function initPasswordToggle() {
    const toggleBtn = document.getElementById('togglePasswordBtn');
    const passwordInput = document.getElementById('id_password');
    if (!toggleBtn || !passwordInput) return;

    toggleBtn.addEventListener('click', (e) => {
        e.preventDefault();
        const isPassword = passwordInput.getAttribute('type') === 'password';
        passwordInput.setAttribute('type', isPassword ? 'text' : 'password');

        const showIcon = toggleBtn.querySelector('.eye-show');
        const hideIcon = toggleBtn.querySelector('.eye-hide');

        if (isPassword) {
            if (showIcon) showIcon.style.display = 'none';
            if (hideIcon) hideIcon.style.display = 'block';
            toggleBtn.setAttribute('aria-label', 'Hide password');
            toggleBtn.setAttribute('title', 'Hide password');
        } else {
            if (showIcon) showIcon.style.display = 'block';
            if (hideIcon) hideIcon.style.display = 'none';
            toggleBtn.setAttribute('aria-label', 'Show password');
            toggleBtn.setAttribute('title', 'Show password');
        }
    });
}

