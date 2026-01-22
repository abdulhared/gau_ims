async function loadTickets() {
    const tableBody = document.querySelector("#ticketsTable tbody");

    try {
        const response = await fetch('http://127.0.0.1:5000/api/tickets');
        const tickets = await response.json();

        tableBody.innerHTML = "";

        tickets.forEach(ticket => {
            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${ticket.std_name}</td>
                <td>${ticket.std_email}</td>
                <td>${ticket.reg_number}</td>
                <td>${ticket.issue_type}</td>
                <td>${new Date(ticket.created_at).toLocaleString()}</td>
            `;

            tableBody.appendChild(row);
        });

    } catch (error) {
        console.error("Error loading tickets:", error);
    }
}

loadTickets();
