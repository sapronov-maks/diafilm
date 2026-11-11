(function () {
  var root = document.documentElement;
  function apply(lang) {
    root.setAttribute('data-lang', lang);
    root.lang = lang;
    var title = root.getAttribute('data-title-' + lang);
    if (title) document.title = title;
  }
  var lang = null;
  try { lang = localStorage.getItem('lang'); } catch (e) {}
  if (lang !== 'ru' && lang !== 'en') {
    lang = /^ru/i.test(navigator.language || '') ? 'ru' : 'en';
  }
  apply(lang);
  document.addEventListener('click', function (e) {
    var t = e.target;
    if (!t || !t.getAttribute) return;
    var set = t.getAttribute('data-set');
    if (set === 'ru' || set === 'en') {
      apply(set);
      try { localStorage.setItem('lang', set); } catch (err) {}
      return;
    }
    if (t.className === 'copy') {
      var text = t.parentNode.querySelector('.addr').textContent.trim();
      var label = t.textContent;
      navigator.clipboard.writeText(text).then(function () {
        t.textContent = t.getAttribute('data-done');
        setTimeout(function () { t.textContent = label; }, 2000);
      });
    }
  });
})();
