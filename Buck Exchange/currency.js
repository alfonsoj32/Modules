function convert() {
    const amount = document.getElementById('amount').value;
    const currency = document.getElementById('currency').value;
    fetch(`https://v6.exchangerate-api.com/v6/71b657bfa87537240d544bae/latest/USD`)
        .then(response => response.json())
        .then(data => {
            const rate = data.conversion_rates[currency];
            if (rate) {
                const result = amount * rate;
                document.getElementById('result').innerHTML = `${amount} USD = ${result.toFixed(2)} ${currency}`;
            } else {
                document.getElementById('result').innerHTML = 'Currency not found!';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

window.onload = function() {
    fetch(`https://v6.exchangerate-api.com/v6/71b657bfa87537240d544bae/latest/USD`)
        .then(response => response.json())
        .then(data => {
            const currencies = Object.keys(data.conversion_rates);
            const selectElement = document.getElementById('currency');
            currencies.forEach(currency => {
                const option = document.createElement('option');
                option.value = currency;
                option.text = currency;
                selectElement.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
};