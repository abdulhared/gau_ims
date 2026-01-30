
const formTicket = document.getElementById('supportForm');

formTicket.addEventListener('submit', async function(e) {
    e.preventDefault();

    const ticketData = {
        stdName: document.getElementById('stdName').value.trim(),
        stdEmail: document.getElementById('stdEmail').value.trim(),
        regNumber: document.getElementById('regNumber').value.trim(),
        issueDescription: document.getElementById('issueDescription').value.trim()
    };

    if (!ticketData.stdName || !ticketData.stdEmail || !ticketData.regNumber || !ticketData.issueDescription) {
        alert("Please fill all fields.");
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/api/ticket/received', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(ticketData)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || "Error submitting");
        } 
    } catch (error) {
        message.style.color = "red";
        message.textContent = error.message || "Server not reachable.";
        console.error(error);
    }
})