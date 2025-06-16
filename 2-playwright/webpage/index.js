// Deterministic seed for each card based on row, column, and time block
function getTimeBlock() {
    return Math.floor(Date.now() / 1000 / 30);
}

function getSeed(rowIndex, colIndex) {
    const timeBlock = getTimeBlock();
    return `${timeBlock}_${rowIndex}_${colIndex}`;
}

function imageUrl(seed) {
    return `https://picsum.photos/seed/${seed}/400/250`;
}

function createImageCard(seed, label) {
    // Deterministically generate a sentence for each card based on row and col
    const deterministicSentences = [
        "The quick brown fox jumps over the lazy dog.",
        "A random fact: honey never spoils.",
        "Did you know? Bananas are berries, but strawberries aren't.",
        "Fun fact: The Eiffel Tower can be 15 cm taller during hot days.",
        "Random tip: Octopuses have three hearts.",
        "Today is a great day to learn something new!",
        "Random info: The longest English word is 189,819 letters long.",
        "Did you know? A group of flamingos is called a 'flamboyance'.",
        "Random trivia: There are more stars in the universe than grains of sand on Earth.",
        "Fact: The heart of a shrimp is located in its head."
    ];
    // The seed is always in the form "timeBlock_row_col"
    const parts = seed.split('_');
    const row = Number(parts[1]);
    const col = Number(parts[2]);
    const idx = (row * 4 + col) % deterministicSentences.length;
    const deterministicText = deterministicSentences[idx];
    return `
        <div class="bg-white rounded-xl shadow p-2 flex flex-col items-center">
            <img src="${imageUrl(seed)}" alt="Random" class="rounded-lg shadow w-full h-40 object-cover mb-2" />
            <div class="text-xs text-gray-500">${deterministicText}</div>
        </div>
    `;
}

function renderImageRow(container, timeBlock, rowIndex, label) {
    let row = document.createElement('div');
    row.className = "grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 mb-6 animate-fade-in";
    for (let col = 0; col < 4; col++) {
        const seed = getSeed(rowIndex, col);
        row.innerHTML += createImageCard(seed, "");
    }
    container.appendChild(row);
}

// Use localStorage to persist the number of rows
function getLoadMoreCount() {
    return parseInt(localStorage.getItem('loadMoreCount') || '0', 10);
}

function setLoadMoreCount(count) {
    localStorage.setItem('loadMoreCount', count);
}

function renderDashboard() {
    const content = document.getElementById('content');
    content.innerHTML = '';
    const loadMoreCount = getLoadMoreCount();
    // Always render the initial row (rowIndex 0)
    renderImageRow(content, 0, 0, "");
    // Render as many "Load More" rows as recorded
    for (let i = 1; i <= loadMoreCount; i++) {
        renderImageRow(content, i, i, "");
    }
}

window.onload = function () {
    renderDashboard();
    setInterval(renderDashboard, 30000);
};

function loadMore() {
    let loadMoreCount = getLoadMoreCount();
    loadMoreCount += 1;
    setLoadMoreCount(loadMoreCount);
    renderDashboard();
}

// Optional: Simple fade-in animation
document.addEventListener('DOMContentLoaded', () => {
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fade-in { from { opacity: 0; } to { opacity: 1; } }
        .animate-fade-in { animation: fade-in 0.5s; }
    `;
    document.head.appendChild(style);
});