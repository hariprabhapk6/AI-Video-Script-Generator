const form = document.getElementById('scriptForm');
const generateBtn = document.getElementById('generateBtn');
const result = document.getElementById('result');
const emptyState = document.getElementById('emptyState');
const errorBox = document.getElementById('error');
let latest = null;
const $ = id => document.getElementById(id);
const escapeHtml = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function listInto(id, items) { $(id).innerHTML = (items || []).map(x => `<li>${escapeHtml(x)}</li>`).join(''); }
form.addEventListener('submit', async e => {
  e.preventDefault();
  errorBox.hidden = true;
  generateBtn.disabled = true;
  generateBtn.innerHTML = '<span>✦</span> Creating your script…';
  const payload = {
    topic: $('topic').value, platform: $('platform').value, tone: $('tone').value,
    audience: $('audience').value, goal: $('goal').value,
    hook_type: $('hook').value, cta_type: $('cta').value
  };
  try {
    const res = await fetch('/generate', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(payload)});
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || 'Could not generate script.');
    latest = data;
    render(data);
  } catch(err) {
    errorBox.textContent = err.message || 'Something went wrong. Please try again.';
    errorBox.hidden = false;
  } finally {
    generateBtn.disabled = false;
    generateBtn.innerHTML = '<span>✦</span> Generate my script <span class="arrow">→</span>';
  }
});
function render(data) {
  emptyState.hidden = true; result.hidden = false;
  $('duration').textContent = data.total_duration_formatted;
  $('words').textContent = data.total_words;
  $('platformOut').textContent = data.platform_label;
  $('scriptSections').innerHTML = Object.entries(data.script).map(([name, text]) => {
    const timing = data.timings[name] || {};
    return `<article class="script-block"><div class="script-title"><h3>${escapeHtml(name.replaceAll('_',' '))}</h3><span class="time-chip">${escapeHtml(timing.duration_formatted || '0:00')} · ${timing.word_count || 0} words</span></div><p>${escapeHtml(text)}</p></article>`;
  }).join('');
  listInto('broll', data.broll_suggestions); listInto('scenes', data.scene_directions);
  listInto('sounds', data.sound_cues); listInto('titles', data.title_suggestions);
  listInto('thumbs', data.thumbnail_suggestions);
  $('description').textContent = data.seo_description;
  $('tags').innerHTML = data.seo_tags.map(t => `<span>#${escapeHtml(t)}</span>`).join('');
  $('copyBtn').disabled = false; $('downloadBtn').disabled = false;
}
$('copyBtn').addEventListener('click', async () => {
  if (!latest) return;
  try { await navigator.clipboard.writeText(latest.formatted_script); $('copyBtn').textContent='Copied!'; setTimeout(()=>$('copyBtn').textContent='Copy',1500); }
  catch { alert('Clipboard access was blocked. You can use Export instead.'); }
});
$('downloadBtn').addEventListener('click', async () => {
  if (!latest) return;
  const blob = new Blob([latest.formatted_script], {type:'text/plain;charset=utf-8'});
  const url = URL.createObjectURL(blob); const a = document.createElement('a');
  a.href=url; a.download='video_script.txt'; a.click(); URL.revokeObjectURL(url);
});
