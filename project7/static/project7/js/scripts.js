const link = document.getElementById('random-cafe-link');
const apiUrl = link.dataset.apiUrl;

link.addEventListener('click', function (e) {
    e.preventDefault();
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error ${response.status}`)
            }
            return response.json();
        })
        .then(data => {
            if (data.cafe && data.cafe.id) {
                window.location.href = `/cafes/${data.cafe.id}/`;
            } else {
                alert('No cafes found.');
            }
        })
        .catch(err => {
            console.error('Error fetching random cafe:', err);
            alert('Something went wrong.');
        });
});
