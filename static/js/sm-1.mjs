function updateForm() {
	const mode = document.querySelector('input[name="mode"]:checked').value;
	const form = document.querySelector('form');
	const button = document.getElementById('go');
	const warning = document.querySelector('.warning');

	form.action = `/sm-1/${mode}`;
	button.textContent = mode === 'decode' ? 'Decode' : 'Encode';
	warning.classList.toggle('show', mode === 'decode');

	console.log('Form after:', form.action);
}

document.addEventListener('DOMContentLoaded', () => {
	updateForm();

	document.querySelectorAll('input[name="mode"]').forEach((radio) => {
		radio.addEventListener('change', updateForm);
	});
});
