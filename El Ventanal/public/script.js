// El Ventanal — Interactive Landing Page Script

document.addEventListener('DOMContentLoaded', () => {
  
  // 1. Copy Email to Clipboard
  const btnCopy = document.getElementById('btnCopy');
  const copyFeedback = document.getElementById('copyFeedback');
  const emailText = 'elv3ntanal@gmail.com';

  if (btnCopy) {
    btnCopy.addEventListener('click', () => {
      navigator.clipboard.writeText(emailText).then(() => {
        copyFeedback.style.display = 'block';
        btnCopy.textContent = '¡Copiado!';
        setTimeout(() => {
          copyFeedback.style.display = 'none';
          btnCopy.textContent = 'Copiar Correo';
        }, 3000);
      }).catch(err => {
        console.error('Error al copiar correo:', err);
      });
    });
  }

  // 2. Interactive Screen Simulator Controls
  const simBtns = document.querySelectorAll('.sim-btn');
  const simSlides = document.querySelectorAll('.sim-slide');

  simBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const mode = btn.getAttribute('data-mode');

      // Update active button
      simBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Update active slide
      simSlides.forEach(slide => {
        slide.classList.remove('active');
        if (slide.id === `slide-${mode}`) {
          slide.classList.add('active');
        }
      });
    });
  });

});

// 3. Form Submission Simulation
function handleFormSubmit(e) {
  e.preventDefault();
  const formSuccess = document.getElementById('formSuccess');
  const form = document.getElementById('contactForm');
  
  if (formSuccess && form) {
    form.style.display = 'none';
    formSuccess.style.display = 'block';
  }
}
