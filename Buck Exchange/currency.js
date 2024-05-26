function convert() {
    const amount = document.getElementById('amount').value;
    const currency = document.getElementById('currency').value;

    // Fetch exchange rates from the API
    fetch(`https://v6.exchangerate-api.com/v6/71b657bfa87537240d544bae/latest/USD`)
        .then(response => response.json())
        .then(data => {
            // Extract the exchange rate for the selected currency
            const rate = data.conversion_rates[currency];
            if (rate) {
                // Calculate the converted amount
                const result = amount * rate;
                document.getElementById('result').innerHTML = `${amount} USD = ${result.toFixed(2)} ${currency}`;
            } else {
                document.getElementById('result').innerHTML = 'Currency not found!';
            }
        })
        .catch(error => {
            // Prompts if there is error during fetch operation
            console.error('Error:', error);
        });
}

window.onload = function() {
    fetch(`https://v6.exchangerate-api.com/v6/71b657bfa87537240d544bae/latest/USD`)
        .then(response => response.json())
        .then(data => {
            // Extract the list of currencies
            const currencies = Object.keys(data.conversion_rates);
            const selectElement = document.getElementById('currency');
            currencies.forEach(currency => {
                const option = document.createElement('option');
                option.value = currency;
                option.text = currency;
                // Add currency options
                selectElement.appendChild(option);
            });
        })
        .catch(error => {
            // Prompts if there is error during fetch operation
            console.error('Error:', error);
        });
};