
const form = document.getElementById('supportForm');
const message = document.getElementById('message');

form.addEventListener('submit', async function(e) {
    e.preventDefault();

    message.textContent = "Submitting...";
    message.style.color = "blue";

    const ticketData = {
        stdName: document.getElementById('stdName').value.trim(),
        stdEmail: document.getElementById('stdEmail').value.trim(),
        regNumber: document.getElementById('regNumber').value.trim(),
        issueDescription: document.getElementById('issueDescription').value.trim()
    };

    // Quick client-side check
    if (!ticketData.stdName || !ticketData.stdEmail || !ticketData.regNumber || !ticketData.issueDescription) {
        message.style.color = "red";
        message.textContent = "Please fill all fields.";
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/api/tickets', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(ticketData)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || "Error submitting ticket");
        }   


        const ticketId = result.ticket_id;

        message.style.color = "green";
        message.textContent = `Ticket submitted successfully! ID: ${ticketId}`;
        form.reset();

    } catch (error) {
        message.style.color = "red";
        message.textContent = error.message || "Server not reachable.";
        console.error(error);
    }
});