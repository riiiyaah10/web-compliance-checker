// Form submission handler
document.getElementById('scanForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const url = document.getElementById('urlInput').value.trim();
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    
    if (!url) {
        alert('Please enter a URL');
        return;
    }
    
    // Show loading state
    loading.classList.remove('d-none');
    results.classList.add('d-none');
    
    try {
        const response = await fetch('/scan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: url })
        });
        
        const data = await response.json();
        
        if (data.success) {
            // Redirect to results page
            window.location.href = `/results?url=${encodeURIComponent(data.url)}`;
        } else {
            alert('Error: ' + (data.error || 'Unknown error occurred'));
            loading.classList.add('d-none');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error scanning website: ' + error.message);
        loading.classList.add('d-none');
    }
});

// URL input validation
document.getElementById('urlInput').addEventListener('input', function(e) {
    let value = e.target.value.trim();
    
    // Auto-add https:// if not present
    if (value && !value.startsWith('http://') && !value.startsWith('https://')) {
        // Only for display purposes
    }
});

// Smooth scroll to results
document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('url')) {
        // Results page - no additional action needed
    }
});
