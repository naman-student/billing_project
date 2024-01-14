
    let transactionCount = 0;

    document.getElementById('addTransaction').addEventListener('click', function() {
        let container = document.getElementById('transactionFormsContainer');
        let template = document.getElementById('transactionFormTemplate').innerHTML;

        // Increment transactionCount to maintain unique names for each field
        transactionCount++;

        // Replace template names with unique names
        let transactionForm = template.replace(/name="([a-zA-Z_]+)"/g, `name="$1_${transactionCount}"`);
        container.innerHTML += transactionForm;
        

    });

    document.getElementById('saveVoucher').addEventListener('click', function() {
        let voucherData = {
            transactions: []
        };

        // Collect voucher specific fields data if any
        // Example: voucherData['date_created'] = document.querySelector('[name="date_created"]').value;

        // Collect transactions data
        let transactionForms = document.querySelectorAll('.transactionForm');
        transactionForms.forEach(function(form, index) {
            let transactionData = {};
            form.querySelectorAll('input, select').forEach(function(input) {
                transactionData[input.name] = input.value;
            });
            voucherData.transactions.push(transactionData);
        });

        // AJAX request to server
        let xhr = new XMLHttpRequest();
        xhr.open('POST', '/path/to/create_voucher/', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken')); // Function to get CSRF token
        xhr.onload = function () {
            if (xhr.status === 200) {
                // Handle success - maybe redirect or clear the form
                console.log('Success:', xhr.responseText);
            } else {
                // Handle error
                console.error('Error:', xhr.status, xhr.statusText);
            }
        };
        xhr.send(JSON.stringify(voucherData));
    });

    // Function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

