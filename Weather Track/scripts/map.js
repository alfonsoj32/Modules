const canvas = document.getElementById('radarMap');
const ctx = canvas.getContext('2d');

async function fetchRadarMap() {
    const response = await fetch('https://api.rainviewer.com/public/weather-maps.json');
    const data = await response.json();
    const latestMap = data[0]; // Assuming the latest map is the first item in the array
    const mapUrl = latestMap.path;

    const image = new Image();
    image.src = mapUrl;
    image.onload = function() {
        canvas.width = image.width;
        canvas.height = image.height;
        ctx.drawImage(image, 0, 0);
    };
}

// Call fetchRadarMap to update the radar map
fetchRadarMap();
