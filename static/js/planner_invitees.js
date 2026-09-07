/**
 * Alex & Divya Wedding Planner — Invitees Dynamic Logic
 * Handles interactive filtering by side & relationship, live headcount calculations, modals, and AJAX operations.
 */

document.addEventListener('DOMContentLoaded', () => {
    // Current Active Filter State
    const filterState = {
        side: 'all',
        relationship: 'all',
        searchQuery: ''
    };

    // DOM Elements
    const searchInput = document.getElementById('inviteeSearchInput');
    const clearSearchBtn = document.getElementById('clearSearchBtn');
    const sideFilterPills = document.querySelectorAll('#sideFilterGroup .filter-pill');
    const relFilterPills = document.querySelectorAll('#relFilterGroup .filter-pill');
    const resetFiltersBtn = document.getElementById('resetFiltersBtn');

    const dynamicFilterCount = document.getElementById('dynamicFilterCount');
    const dynamicGuestCount = document.getElementById('dynamicGuestCount');
    const activeFilterIndicators = document.getElementById('activeFilterIndicators');
    const filterEmptyState = document.getElementById('filterEmptyState');
    const tableBody = document.getElementById('inviteesTableBody');
    const tableCard = document.querySelector('.table-card');

    const modalBackdrop = document.getElementById('inviteeModalBackdrop');
    const deleteModalBackdrop = document.getElementById('deleteModalBackdrop');
    const inviteeForm = document.getElementById('inviteeForm');
    const openAddModalBtn = document.getElementById('openAddModalBtn');
    const closeModalBtn = document.getElementById('closeModalBtn');

    // Get CSRF Token
    function getCsrfToken() {
        const csrfInput = document.querySelector('[name=csrfmiddlewaretoken]');
        return csrfInput ? csrfInput.value : '';
    }

    /* -------------------------------------------------------------------------- */
    /* Dynamic Filtering & Count Recalculation                                    */
    /* -------------------------------------------------------------------------- */
    function applyFilters() {
        const rows = document.querySelectorAll('.invitee-row');
        let visibleInvitees = 0;
        let visibleGuests = 0;

        const query = filterState.searchQuery.toLowerCase().trim();
        const activeSide = filterState.side;
        const activeRel = filterState.relationship;

        rows.forEach(row => {
            const rowName = (row.getAttribute('data-name') || '').toLowerCase();
            const rowSide = row.getAttribute('data-side') || '';
            const rowRel = row.getAttribute('data-rel') || '';
            const rowGuests = parseInt(row.getAttribute('data-guests') || '1', 10);

            // Match conditions
            const matchesSide = (activeSide === 'all') || (rowSide === activeSide);
            const matchesRel = (activeRel === 'all') || (rowRel === activeRel);
            const matchesSearch = !query || 
                rowName.includes(query);

            if (matchesSide && matchesRel && matchesSearch) {
                row.style.display = '';
                visibleInvitees++;
                visibleGuests += rowGuests;
            } else {
                row.style.display = 'none';
            }
        });

        // Update Dynamic Count Banner
        if (dynamicFilterCount) dynamicFilterCount.textContent = visibleInvitees;
        if (dynamicGuestCount) dynamicGuestCount.textContent = visibleGuests;

        // Toggle Empty Filter State
        if (filterEmptyState) {
            if (visibleInvitees === 0 && rows.length > 0) {
                filterEmptyState.style.display = 'flex';
            } else {
                filterEmptyState.style.display = 'none';
            }
        }

        // Render Active Filter Tag Indicators
        updateActiveFilterPills();
    }

    function updateActiveFilterPills() {
        if (!activeFilterIndicators) return;
        activeFilterIndicators.innerHTML = '';

        const tags = [];
        if (filterState.side !== 'all') {
            tags.push(`Side: ${filterState.side.toUpperCase()}`);
        }
        if (filterState.relationship !== 'all') {
            tags.push(`Rel: ${filterState.relationship.toUpperCase()}`);
        }
        if (filterState.searchQuery) {
            tags.push(`Search: "${filterState.searchQuery}"`);
        }

        tags.forEach(tagText => {
            const tag = document.createElement('span');
            tag.className = 'filter-tag-mini';
            tag.textContent = tagText;
            activeFilterIndicators.appendChild(tag);
        });

        // Reset Button Visibility
        const isFiltered = (filterState.side !== 'all' || filterState.relationship !== 'all' || filterState.searchQuery !== '');
        if (resetFiltersBtn) {
            resetFiltersBtn.style.display = isFiltered ? 'inline-flex' : 'none';
        }
    }

    /* -------------------------------------------------------------------------- */
    /* Filter Event Listeners                                                     */
    /* -------------------------------------------------------------------------- */
    // Side Filter Pills
    sideFilterPills.forEach(pill => {
        pill.addEventListener('click', () => {
            sideFilterPills.forEach(p => {
                p.classList.remove('active');
                p.setAttribute('aria-checked', 'false');
            });
            pill.classList.add('active');
            pill.setAttribute('aria-checked', 'true');

            filterState.side = pill.getAttribute('data-side') || 'all';
            applyFilters();
        });
    });

    // Relationship Filter Pills
    relFilterPills.forEach(pill => {
        pill.addEventListener('click', () => {
            relFilterPills.forEach(p => {
                p.classList.remove('active');
                p.setAttribute('aria-checked', 'false');
            });
            pill.classList.add('active');
            pill.setAttribute('aria-checked', 'true');

            filterState.relationship = pill.getAttribute('data-rel') || 'all';
            applyFilters();
        });
    });

    // Search Input Debounce
    let searchTimeout = null;
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const val = e.target.value;
            if (clearSearchBtn) {
                clearSearchBtn.style.display = val.length > 0 ? 'block' : 'none';
            }
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                filterState.searchQuery = val;
                applyFilters();
            }, 120);
        });
    }

    if (clearSearchBtn) {
        clearSearchBtn.addEventListener('click', () => {
            searchInput.value = '';
            clearSearchBtn.style.display = 'none';
            filterState.searchQuery = '';
            applyFilters();
            searchInput.focus();
        });
    }

    // Reset All Filters
    window.resetAllFilters = function() {
        filterState.side = 'all';
        filterState.relationship = 'all';
        filterState.searchQuery = '';

        if (searchInput) {
            searchInput.value = '';
            if (clearSearchBtn) clearSearchBtn.style.display = 'none';
        }

        sideFilterPills.forEach(p => {
            const isAll = p.getAttribute('data-side') === 'all';
            p.classList.toggle('active', isAll);
            p.setAttribute('aria-checked', isAll ? 'true' : 'false');
        });

        relFilterPills.forEach(p => {
            const isAll = p.getAttribute('data-rel') === 'all';
            p.classList.toggle('active', isAll);
            p.setAttribute('aria-checked', isAll ? 'true' : 'false');
        });

        applyFilters();
    };

    if (resetFiltersBtn) {
        resetFiltersBtn.addEventListener('click', window.resetAllFilters);
    }

    /* -------------------------------------------------------------------------- */
    /* Modal Management (Add / Edit)                                              */
    /* -------------------------------------------------------------------------- */
    window.openAddModal = function() {
        if (!modalBackdrop || !inviteeForm) return;
        inviteeForm.reset();
        document.getElementById('inviteeId').value = '';
        document.getElementById('modalTitle').textContent = 'Add New Invitee';
        document.getElementById('modalBadge').textContent = 'New Guest Entry';
        document.getElementById('submitBtnText').textContent = 'Save Invitee';
        inviteeForm.action = '/invitees/add/';
        document.getElementById('id_guest_count').value = 1;

        // Auto-select filter values if active
        if (filterState.side !== 'all') {
            document.getElementById('id_side').value = filterState.side;
        }
        if (filterState.relationship !== 'all') {
            document.getElementById('id_relationship').value = filterState.relationship;
        }

        modalBackdrop.classList.add('open');
        modalBackdrop.setAttribute('aria-hidden', 'false');
        setTimeout(() => document.getElementById('id_name').focus(), 150);
    };

    if (openAddModalBtn) {
        openAddModalBtn.addEventListener('click', window.openAddModal);
    }

    window.openEditModal = function(inviteeId) {
        if (!modalBackdrop || !inviteeForm) return;

        fetch(`/invitees/${inviteeId}/edit/`, {
            headers: { 'X-Requested-With': 'XMLHttpRequest' }
        })
        .then(res => res.json())
        .then(data => {
            if (data.status === 'success' && data.invitee) {
                const inv = data.invitee;
                document.getElementById('inviteeId').value = inv.id;
                document.getElementById('id_name').value = inv.name;
                document.getElementById('id_side').value = inv.side;
                document.getElementById('id_relationship').value = inv.relationship;
                document.getElementById('id_guest_count').value = inv.guest_count;
                document.getElementById('id_events_invited').value = inv.events_invited || 'all';

                document.getElementById('modalTitle').textContent = 'Edit Invitee';
                document.getElementById('modalBadge').textContent = 'Update Record';
                document.getElementById('submitBtnText').textContent = 'Update Invitee';
                inviteeForm.action = `/invitees/${inv.id}/edit/`;

                modalBackdrop.classList.add('open');
                modalBackdrop.setAttribute('aria-hidden', 'false');
                setTimeout(() => document.getElementById('id_name').focus(), 150);
            } else {
                window.showToast('Could not load invitee data.', 'error');
            }
        })
        .catch(() => {
            window.showToast('Network error loading invitee.', 'error');
        });
    };

    window.closeModal = function() {
        if (!modalBackdrop) return;
        modalBackdrop.classList.remove('open');
        modalBackdrop.setAttribute('aria-hidden', 'true');
    };

    if (closeModalBtn) closeModalBtn.addEventListener('click', window.closeModal);

    window.stepGuestCount = function(delta) {
        const input = document.getElementById('id_guest_count');
        if (!input) return;
        let current = parseInt(input.value || '1', 10);
        current = Math.max(1, Math.min(99, current + delta));
        input.value = current;
    };

    // Form Submit via AJAX
    if (inviteeForm) {
        inviteeForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const submitBtn = document.getElementById('saveInviteeSubmitBtn');
            const origText = document.getElementById('submitBtnText').textContent;
            document.getElementById('submitBtnText').textContent = 'Saving...';
            if (submitBtn) submitBtn.disabled = true;

            const formData = new FormData(inviteeForm);

            fetch(inviteeForm.action, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': getCsrfToken()
                },
                body: formData
            })
            .then(res => res.json())
            .then(data => {
                if (data.status === 'success') {
                    window.closeModal();
                    window.showToast(data.message, 'success');
                    // Reload data or page to sync all metric totals smoothly
                    setTimeout(() => window.location.reload(), 300);
                } else {
                    let errMsg = 'Please check the form for errors.';
                    if (data.errors) {
                        errMsg = Object.values(data.errors).flat().join(' ');
                    }
                    window.showToast(errMsg, 'error');
                }
            })
            .catch(() => {
                // Fallback normal submission if ajax fails
                inviteeForm.submit();
            })
            .finally(() => {
                if (submitBtn) submitBtn.disabled = false;
                document.getElementById('submitBtnText').textContent = origText;
            });
        });
    }

    /* -------------------------------------------------------------------------- */
    /* Delete Confirmation Modal                                                  */
    /* -------------------------------------------------------------------------- */
    let currentDeleteId = null;

    window.confirmDeleteInvitee = function(id, name) {
        currentDeleteId = id;
        const nameEl = document.getElementById('deleteInviteeName');
        const deleteForm = document.getElementById('deleteForm');
        if (nameEl) nameEl.textContent = name;
        if (deleteForm) deleteForm.action = `/invitees/${id}/delete/`;

        if (deleteModalBackdrop) {
            deleteModalBackdrop.classList.add('open');
            deleteModalBackdrop.setAttribute('aria-hidden', 'false');
        }
    };

    window.closeDeleteModal = function() {
        if (!deleteModalBackdrop) return;
        deleteModalBackdrop.classList.remove('open');
        deleteModalBackdrop.setAttribute('aria-hidden', 'true');
        currentDeleteId = null;
    };

    const deleteForm = document.getElementById('deleteForm');
    if (deleteForm) {
        deleteForm.addEventListener('submit', (e) => {
            e.preventDefault();
            if (!currentDeleteId) return;

            fetch(`/invitees/${currentDeleteId}/delete/`, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': getCsrfToken()
                }
            })
            .then(res => res.json())
            .then(data => {
                if (data.status === 'success') {
                    window.closeDeleteModal();
                    window.showToast(data.message, 'success');
                    const row = document.querySelector(`.invitee-row[data-id="${currentDeleteId}"]`);
                    if (row) row.remove();
                    setTimeout(() => window.location.reload(), 250);
                }
            })
            .catch(() => {
                deleteForm.submit();
            });
        });
    }

    // Close modals on backdrop click or ESC key
    window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            window.closeModal();
            window.closeDeleteModal();
        }
    });

    [modalBackdrop, deleteModalBackdrop].forEach(backdrop => {
        if (backdrop) {
            backdrop.addEventListener('click', (e) => {
                if (e.target === backdrop) {
                    window.closeModal();
                    window.closeDeleteModal();
                }
            });
        }
    });

    // Initial Filter Calculation on page load
    applyFilters();
});
