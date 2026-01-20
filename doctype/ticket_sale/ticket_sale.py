import frappe
from frappe.model.document import Document

class TicketSale(Document):

    def validate(self):
        if not self.event or not self.quantity:
            return

        event = frappe.get_doc("Event Detail", self.event)

        # -------- 1. CAPACITY BLOCKING --------
        sold = event.tickets_sold or 0
        capacity = event.capacity or 0

        if sold + self.quantity > capacity:
            frappe.throw(
                f"Event capacity exceeded. Available seats: {capacity - sold}"
            )

        # -------- 2. REVENUE CALCULATION --------
        ticket_price = event.ticket_price or 0
        self.total_price = ticket_price * self.quantity


    def on_submit(self):
        event = frappe.get_doc("Event Detail", self.event)

        # -------- 3. AUTO TICKET COUNT --------
        event.tickets_sold = (event.tickets_sold or 0) + self.quantity

        # -------- 4. REMAINING CAPACITY --------
        event.remaining_capacity = event.capacity - event.tickets_sold
        event.save()
