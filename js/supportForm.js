const form = document.getElementById('supportForm');
const message = document.getElementById('message');

form.addEventListener('submit', async function(e) {
    e.preventDefault();

    const ticketData = {
        stdName: document.getElementById('stdName').value,
        stdEmail: document.getElementById('stdEmail').value,
        regNumber: document.getElementById('regNumber').value,
        issueDescription: document.getElementById('issueDescription').value
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/api/tickets', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(ticketData)
        });

        const result = await response.json();

        if (response.ok) {
            message.style.color = "green";
            message.textContent = "Ticket submitted successfully! ID: " + result.ticket_id;
            form.reset();
        } else {
            message.style.color = "red";
            message.textContent = "Error submitting ticket.";
        }

    } catch (error) {
        message.style.color = "red";
        message.textContent = "Server not reachable.";
        console.error(error);
    }
});
