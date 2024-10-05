function resetBestScore() {
    fetch('/reset_best_score', { method: 'POST' })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            location.href = '/';
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}