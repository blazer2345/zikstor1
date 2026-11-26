import { pages } from './storage.js';

let displayHTML = '';
pages.forEach((page) => {
  displayHTML += `
        <div class="app-card">
        
        <img class="images-1" src="${window.imagePath}${page.image}" alt="">
      <p class="text1">${page.name}</p>

      <p class="description">${page.description}</p>
      
     <button 
     class="app-button"
     onclick="window.location.href='${page.url}'">
     ${page.button}
     </button>

      </div>
  `; 
});
document.querySelector('.display-grid').innerHTML = displayHTML;

      