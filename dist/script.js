let duasData = [];
let currentFilter = 'Semua';
let currentSearch = '';
let currentPage = 1;
const itemsPerPage = 10;
let activeDuaId = null;
let bookmarks = JSON.parse(localStorage.getItem('nurhira_bookmarks')) || [];
let currentLang = 'ms';
let modalToggles = JSON.parse(localStorage.getItem('modal_toggles')) || {
  source: true,
  definition: true,
  rumi: true,
  meaning: true,
  fadhilat: true
};

const uiTexts = {
  source: "Sumber",
  rumi: "Bacaan Rumi",
  fullView: "Tekan untuk paparan penuh",
  meaning: "Maksud",
  fadhilat: "Fadhilat",
  searchPlaceholder: "🔍 Cari doa...",
  noDuas: "📭 Tiada doa dijumpai.",
  copied: "✨ Doa berjaya disalin ke papan klip!"
};

function getUI(key) {
  return uiTexts[key] || key;
}

async function loadDuasData() {
  try {
    // Try localStorage first
    const storageKey = `duas_data_${currentLang}`;
    const localData = localStorage.getItem(storageKey);

    if (localData) {
      duasData = JSON.parse(localData);
    } else {
      // Fallback to JSON file
      let fileName = 'duas.json';
      if (currentLang === 'en') fileName = 'en-duas.json';
      else if (currentLang === 'cn') fileName = 'cn-duas.json';
      else if (currentLang === 'ta') fileName = 'ta-duas.json';

      const res = await fetch(fileName + '?v=' + Date.now());
      duasData = await res.json();
    }

    const searchInput = document.getElementById('searchInput');
    if (searchInput) searchInput.placeholder = getUI('searchPlaceholder');

    renderDuas();
  } catch (err) {
    console.error('Gagal memuatkan data doa:', err);
  }
}

document.addEventListener('DOMContentLoaded', async () => {
  await loadDuasData();

  // Search input listener
  document.getElementById('searchInput').addEventListener('input', (e) => {
    currentSearch = e.target.value.toLowerCase();
    currentPage = 1; // reset to page 1 on search
    renderDuas();
  });
});

function getLocalized(val) {
  if (!val) return '';
  if (typeof val === 'object') {
    return val['ms'] || Object.values(val)[0] || '';
  }
  return val;
}

function toggleCategoryMenu() {
  const dropdown = document.getElementById('categoryDropdown');
  dropdown.classList.toggle('hidden');
}

function toggleSubmenu(e) {
  e.stopPropagation();
  const sub = document.getElementById('niatSolatSubmenu');
  sub.classList.toggle('hidden');
}

// Close dropdown when clicking outside
window.addEventListener('click', (e) => {
  const dropdown = document.getElementById('categoryDropdown');
  const btn = e.target.closest('button');
  if (!e.target.closest('#categoryDropdown') && (!btn || !btn.getAttribute('onclick')?.includes('toggleCategoryMenu'))) {
    if (dropdown && !dropdown.classList.contains('hidden')) {
      dropdown.classList.add('hidden');
    }
  }
});

function selectCategory(cat) {
  currentFilter = cat;
  currentPage = 1; // reset to page 1 on filter change
  document.getElementById('categoryDropdown').classList.add('hidden');

  const badge = document.getElementById('activeCategoryBadge');
  if (badge) {
    badge.innerText = cat;
  }

  renderDuas();
}

function renderDuas() {
  const container = document.getElementById('duasContainer');
  container.innerHTML = '';

  let filtered = duasData.filter(dua => {
    const catMatch = Array.isArray(dua.category) ? dua.category.includes(currentFilter) : dua.category === currentFilter;
    const matchesCat = currentFilter === 'Semua' ||
                       (currentFilter === 'Favorit' && bookmarks.includes(dua.id)) ||
                       catMatch;

    const matchesSearch = dua.title.toLowerCase().includes(currentSearch) ||
                          dua.rumi.toLowerCase().includes(currentSearch) ||
                          dua.meaning.toLowerCase().includes(currentSearch) ||
                          (dua.source && dua.source.toLowerCase().includes(currentSearch));

    return matchesCat && matchesSearch;
  }).slice().reverse();

  const totalPages = Math.ceil(filtered.length / itemsPerPage) || 1;
  if (currentPage > totalPages) currentPage = totalPages;
  if (currentPage < 1) currentPage = 1;

  // Pagination slice
  const start = (currentPage - 1) * itemsPerPage;
  const paginatedItems = filtered.slice(start, start + itemsPerPage);

  // Render side-scroll pagination buttons (1, 2, 3...)
  const paginationContainer = document.getElementById('paginationContainer');
  const bottomPaginationContainer = document.getElementById('bottomPaginationContainer');

  if (filtered.length > itemsPerPage) {
    paginationContainer.classList.remove('hidden');
    bottomPaginationContainer.classList.remove('hidden');

    let pagesHTML = '';
    for (let i = 1; i <= totalPages; i++) {
      const isActive = i === currentPage;
      const btnClass = isActive
        ? 'px-4 py-2 rounded-xl text-xs font-bold bg-neonPink text-white shadow-neon transition-all flex-shrink-0'
        : 'px-4 py-2 rounded-xl text-xs font-semibold glass-card text-gray-300 hover:text-white transition-all flex-shrink-0';
      pagesHTML += `<button onclick="goToPage(${i})" class="${btnClass}">${i}</button>`;
    }

    paginationContainer.innerHTML = pagesHTML;
    bottomPaginationContainer.innerHTML = pagesHTML;
  } else {
    paginationContainer.classList.add('hidden');
    bottomPaginationContainer.classList.add('hidden');
  }

  if (paginatedItems.length === 0) {
    container.innerHTML = `
      <div class="col-span-full text-center py-12 glass-card rounded-2xl">
        <p class="text-gray-400 text-sm">${getUI('noDuas')}</p>
      </div>
    `;
    return;
  }

  paginatedItems.forEach(dua => {
    const isFav = bookmarks.includes(dua.id);
    const card = document.createElement('div');
    card.className = 'glass-card rounded-2xl p-5 flex flex-col justify-between cursor-pointer group relative overflow-hidden';
    card.onclick = () => openModal(dua.id);

    card.innerHTML = `
      <div>
        <!-- Top bar: Category & Bookmark -->
        <div class="flex items-center justify-between mb-2">
          <span class="text-[10px] uppercase tracking-widest px-2.5 py-1 rounded-lg bg-pink-500/10 text-pink-400 border border-pink-500/20 font-semibold"><i class="fa-solid fa-tag mr-1"></i> ${Array.isArray(dua.category) ? dua.category.join(' • ') : dua.category}</span>
          <button onclick="event.stopPropagation(); toggleBookmark(${dua.id})" class="text-gray-400 hover:text-neonPink transition-colors p-1">
            <span class="${isFav ? 'text-neonPink font-bold text-base' : 'text-gray-400 text-base'}">
              <i class="${isFav ? 'fa-solid fa-star' : 'fa-regular fa-star'}"></i>
            </span>
          </button>
        </div>

        <!-- Title -->
        <div class="flex items-center gap-2 mb-1">
          <span class="text-[8px] text-green-400 font-mono px-1.5 py-0.5 rounded bg-green-950/40 border border-green-500/30">#${dua.id}</span>
          <h3 class="text-lg font-bold text-white group-hover:text-pink-300 transition-colors">📖 ${getLocalized(dua.title)}</h3>
        </div>

        <!-- Source / Rujukan -->
        ${dua.showSource !== false && dua.source ? `
        <div class="mb-3">
          <span class="text-[10px] text-neonCyan font-medium bg-cyan-950/40 px-2 py-0.5 rounded border border-cyan-500/20 inline-block"><i class="fa-solid fa-book-bookmark mr-1"></i> ${getUI('source')}: ${dua.source}</span>
        </div>` : ''}

        <!-- Arabic Text (22px white) -->
        <div class="bg-black/40 border border-pink-500/20 rounded-xl p-4 mb-3 text-right">
          <p class="text-[22px] font-arabic text-white leading-loose line-clamp-2">${dua.arabic}</p>
        </div>

        <!-- Bacaan Rumi Text (12px yellow, whitespace-pre-line, 100 char limit) -->
        <div class="mb-3">
          <span class="text-[10px] text-neonCyan font-semibold uppercase tracking-wider block mb-0.5"><i class="fa-solid fa-font mr-1"></i> ${getUI('rumi')}</span>
          <p class="text-[12px] text-yellow-400 italic font-light leading-relaxed line-clamp-2 whitespace-pre-line">${dua.rumi.substring(0, 100)}${dua.rumi.length > 100 ? '...' : ''}</p>
        </div>
      </div>

      <!-- Footer Prompt -->
      <div class="mt-2 pt-3 border-t border-pink-500/10 flex items-center justify-between text-xs text-neonCyan font-medium">
        <span><i class="fa-regular fa-hand-pointer mr-1"></i> ${getUI('fullView')}</span>
        <span class="group-hover:translate-x-1 transition-transform">→</span>
      </div>
    `;
    container.appendChild(card);
  });
}

function goToPage(pageNumber) {
  currentPage = pageNumber;
  renderDuas();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function openModal(id) {
  const dua = duasData.find(d => d.id === id);
  if (!dua) return;
  activeDuaId = id;

  document.getElementById('modalCategory').innerHTML = `<i class="fa-solid fa-tag mr-1"></i> ${Array.isArray(dua.category) ? dua.category.join(' • ') : dua.category}`;
  document.getElementById('modalTitle').innerHTML = `<span class="text-[8px] text-green-400 font-mono px-1.5 py-0.5 rounded bg-green-950/40 border border-green-500/30 mr-2">#${dua.id}</span> 📖 ${getLocalized(dua.title)}`;
  const sourceContainer = document.getElementById('modalSource').parentElement;
  if (dua.showSource !== false && dua.source) {
    document.getElementById('modalSource').innerHTML = `<i class="fa-solid fa-book-bookmark mr-1"></i> ${getUI('source')}: ${dua.source}`;
    sourceContainer.classList.remove('hidden');
  } else {
    sourceContainer.classList.add('hidden');
  }

  // Update modal static UI label headers
  const modalRumiLabel = document.getElementById('modalRumiLabel');
  if (modalRumiLabel) modalRumiLabel.innerHTML = `<i class="fa-solid fa-font mr-1"></i> ${getUI('rumi')}`;

  const modalMeaningLabel = document.getElementById('modalMeaningLabel');
  if (modalMeaningLabel) modalMeaningLabel.innerHTML = `<i class="fa-solid fa-language mr-1"></i> ${getUI('meaning')}`;

  const modalFadhilatLabel = document.getElementById('modalFadhilatLabel');
  if (modalFadhilatLabel) modalFadhilatLabel.innerHTML = `<i class="fa-solid fa-star mr-1"></i> ${getUI('fadhilat')}`;

  document.getElementById('modalArabic').innerText = dua.arabic;
  document.getElementById('modalRumi').innerText = dua.rumi;
  document.getElementById('modalMeaning').innerText = getLocalized(dua.meaning);

  const rawatibDefEl = document.getElementById('modalRawatibDef');
  if (dua.definition) {
    rawatibDefEl.innerText = getLocalized(dua.definition);
    rawatibDefEl.classList.remove('hidden');
  } else {
    const isRawatib = Array.isArray(dua.category) && dua.category.includes('Rawatib');
    if (isRawatib) {
      rawatibDefEl.innerText = "Definisi Solat Rawatib: Solat sunat yang dikerjakan mengiringi solat fardhu lima waktu...";
      rawatibDefEl.classList.remove('hidden');
    } else {
      rawatibDefEl.classList.add('hidden');
    }
  }

  const fadhilatContainer = document.getElementById('modalFadhilatContainer');
  if (dua.fadhilat) {
    document.getElementById('modalFadhilatText').innerText = getLocalized(dua.fadhilat);
    fadhilatContainer.classList.remove('hidden');
  } else {
    fadhilatContainer.classList.add('hidden');
  }

  updateModalBookmarkBtn();

  const modal = document.getElementById('duaModal');
  const box = document.getElementById('modalContentBox');
  modal.classList.remove('hidden');
  setTimeout(() => {
    modal.classList.remove('opacity-0');
    box.classList.remove('scale-95');
    box.classList.add('scale-100');
    updateModalSections();
  }, 10);
}

function closeModal() {
  const modal = document.getElementById('duaModal');
  const box = document.getElementById('modalContentBox');
  modal.classList.add('opacity-0');
  box.classList.remove('scale-100');
  box.classList.add('scale-95');
  setTimeout(() => {
    modal.classList.add('hidden');
    activeDuaId = null;
  }, 300);
}

function toggleBookmark(id) {
  if (bookmarks.includes(id)) {
    bookmarks = bookmarks.filter(b => b !== id);
  } else {
    bookmarks.push(id);
  }
  localStorage.setItem('nurhira_bookmarks', JSON.stringify(bookmarks));
  renderDuas();
  if (activeDuaId === id) {
    updateModalBookmarkBtn();
  }
}

function toggleBookmarkCurrent() {
  if (activeDuaId !== null) {
    toggleBookmark(activeDuaId);
  }
}

function updateModalBookmarkBtn() {
  const isFav = bookmarks.includes(activeDuaId);
  const icon = document.getElementById('modalFavIcon');
  const btn = document.getElementById('modalFavBtn');
  if (isFav) {
    icon.innerHTML = '<i class="fa-solid fa-star"></i>';
    btn.className = 'px-4 py-2 rounded-xl text-xs font-semibold glass-card text-neonPink border-neonPink/50 bg-pink-500/10 transition-all flex items-center gap-2';
  } else {
    icon.innerHTML = '<i class="fa-regular fa-star"></i>';
    btn.className = 'px-4 py-2 rounded-xl text-xs font-semibold glass-card text-pink-400 hover:bg-pink-500/20 transition-all flex items-center gap-2';
  }
}

function copyCurrentDua() {
  const dua = duasData.find(d => d.id === activeDuaId);
  if (!dua) return;
  let text = `${dua.title}${dua.showSource !== false && dua.source ? ` (${getUI('source')}: ${dua.source})` : ''}\n\n${dua.arabic}\n\n${dua.rumi}\n\n${getUI('meaning')}: ${dua.meaning}`;
  if (dua.definition) {
    text += `\n\nDefinisi: ${dua.definition}`;
  }
  if (dua.fadhilat) {
    text += `\n\n${getUI('fadhilat')}:\n${dua.fadhilat}`;
  }
  navigator.clipboard.writeText(text).then(() => {
    alert(getUI('copied'));
  });
}

// Close modal on background click
document.getElementById('duaModal').addEventListener('click', (e) => {
  if (e.target.id === 'duaModal') {
    closeModal();
  }
});

function toggleModalSection(section) {
  modalToggles[section] = !modalToggles[section];
  localStorage.setItem('modal_toggles', JSON.stringify(modalToggles));
  updateModalSections();
}

function updateModalSections() {
  const sourceSection = document.getElementById('modalSource').parentElement;
  const defSection = document.getElementById('modalDefinitionSection');
  const rumiSection = document.getElementById('modalRumiSection');
  const meaningSection = document.getElementById('modalMeaningBlock');
  const fadhilatSection = document.getElementById('modalFadhilatContainer');

  const sourceBtn = document.getElementById('toggleSourceBtn');
  const defBtn = document.getElementById('toggleDefBtn');
  const rumiBtn = document.getElementById('toggleRumiBtn');
  const meaningBtn = document.getElementById('toggleMeaningBtn');
  const fadhilatBtn = document.getElementById('toggleFadhilatBtn');

  // Update visibility
  if (sourceSection) {
    sourceSection.style.display = modalToggles.source ? 'block' : 'none';
  }
  if (defSection) {
    defSection.style.display = modalToggles.definition ? 'block' : 'none';
  }
  if (rumiSection) {
    rumiSection.style.display = modalToggles.rumi ? 'block' : 'none';
  }
  if (meaningSection) {
    meaningSection.style.display = modalToggles.meaning ? 'block' : 'none';
  }
  if (fadhilatSection) {
    const dua = duasData.find(d => d.id === activeDuaId);
    if (dua && dua.fadhilat && modalToggles.fadhilat) {
      fadhilatSection.style.display = 'block';
      fadhilatSection.classList.remove('hidden');
    } else {
      fadhilatSection.style.display = 'none';
      fadhilatSection.classList.add('hidden');
    }
  }

  // Update button opacity
  if (sourceBtn) sourceBtn.style.opacity = modalToggles.source ? '1' : '0.4';
  if (defBtn) defBtn.style.opacity = modalToggles.definition ? '1' : '0.4';
  if (rumiBtn) rumiBtn.style.opacity = modalToggles.rumi ? '1' : '0.4';
  if (meaningBtn) meaningBtn.style.opacity = modalToggles.meaning ? '1' : '0.4';
  if (fadhilatBtn) fadhilatBtn.style.opacity = modalToggles.fadhilat ? '1' : '0.4';
}
