// Select table body ONCE (used by both functions)
const tableBody = document.querySelector("#ticketsTable tbody");

/**
 * Fetch tickets from Flask and render table
 */
async function loadTickets() {
    try {
        const response = await fetch("http://127.0.0.1:5000/api/tickets/list");

        if (!response.ok) {
            throw new Error("Failed to fetch tickets");
        }

        const tickets = await response.json();
        tableBody.innerHTML = "";

        tickets.forEach(ticket => {
            const row = document.createElement("tr");

            row.innerHTML = `
                
                <td data-label="Reg Number">${ticket.reg_number}</td>
                <td data-label="Issue">${ticket.issue_type}</td>
                <td data-label="Date">
                    ${new Date(ticket.created_at).toLocaleString()}
                </td>
                
                <td data-label="Actions" class="actions">
                    <button 
                        class="btn tick" 
                        data-ticket-id="${ticket.id}">
                        ✔
                    </button>

                    <button 
                        class="btn email" 
                        data-ticket-id="${ticket.id}">
                        mail
                    </button>
                </td>
            `;

            tableBody.appendChild(row);
        });

    } catch (error) {
        // console.error("Error loading tickets:", error);
        console.log("Ticket object:", ticket);
        
    }
}

/**
 * Event delegation for dynamic buttons
 */
tableBody.addEventListener("click", function (e) {
    const target = e.target;

    // ✔ Resolve ticket
    if (target.classList.contains("tick")) {  
        const payload = {
            ticket_id: target.dataset.ticketId,
            action: "resolve"
        };

        console.log("Payload to send:", payload);
    }

    // ✉ Send email
    if (target.classList.contains("email")) {
        const payload = {
            ticket_id: target.dataset.ticketId,
            action: "send_email"
        };

        console.log("Payload to send:", payload);
    }
});

// Load tickets when page loads
loadTickets();
