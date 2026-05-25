"""
Electrical Workshop Management System
Main application entry point
"""

import sys
from calculations.electrical_calculations import ElectricalCalculations
from inventory_manager.equipment import InventoryManager, Equipment, EquipmentStatus
from circuit_simulator.circuit import Circuit, Component, ComponentType
from scheduler.workshop_scheduler import WorkshopScheduler, Session
from documentation.doc_generator import DocumentationManager, TechnicalDocument, DocumentationType


class WorkshopManagementSystem:
    """
    Main workshop management system
    Integrates all modules
    """
    
    def __init__(self):
        """Initialize the workshop management system"""
        self.calc = ElectricalCalculations()
        self.inventory = InventoryManager()
        self.circuits = {}
        self.scheduler = WorkshopScheduler()
        self.documentation = DocumentationManager()
        self.is_running = True
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("ELECTRICAL WORKSHOP MANAGEMENT SYSTEM")
        print("="*50)
        print("\n1. Electrical Calculations")
        print("2. Equipment Inventory Management")
        print("3. Circuit Simulation")
        print("4. Workshop Scheduling")
        print("5. Documentation System")
        print("6. System Information")
        print("0. Exit")
        print("-"*50)
    
    def show_calculations_menu(self):
        """Display calculations menu"""
        print("\n--- Electrical Calculations ---")
        print("1. Ohm's Law (Voltage)")
        print("2. Ohm's Law (Current)")
        print("3. Ohm's Law (Resistance)")
        print("4. Power Calculation")
        print("5. Series Resistance")
        print("6. Parallel Resistance")
        print("7. Back to Main Menu")
    
    def show_inventory_menu(self):
        """Display inventory menu"""
        print("\n--- Equipment Inventory Management ---")
        print("1. Add Equipment")
        print("2. View All Equipment")
        print("3. Update Quantity")
        print("4. Update Status")
        print("5. View Total Inventory Value")
        print("6. View Low Stock Items")
        print("7. Back to Main Menu")
    
    def show_circuit_menu(self):
        """Display circuit menu"""
        print("\n--- Circuit Simulation ---")
        print("1. Create New Circuit")
        print("2. List All Circuits")
        print("3. Simulate Series Circuit")
        print("4. Simulate Parallel Circuit")
        print("5. Back to Main Menu")
    
    def show_scheduler_menu(self):
        """Display scheduler menu"""
        print("\n--- Workshop Scheduling ---")
        print("1. Create New Session")
        print("2. List All Sessions")
        print("3. Register Participant")
        print("4. View Session Details")
        print("5. View Upcoming Sessions")
        print("6. Back to Main Menu")
    
    def show_documentation_menu(self):
        """Display documentation menu"""
        print("\n--- Documentation System ---")
        print("1. Create New Document")
        print("2. List All Documents")
        print("3. Search by Title")
        print("4. View Document Statistics")
        print("5. Export Document")
        print("6. Back to Main Menu")
    
    def handle_calculations(self):
        """Handle calculations menu"""
        while True:
            self.show_calculations_menu()
            choice = input("\nSelect option: ")
            
            if choice == "1":
                try:
                    current = float(input("Enter current (A): "))
                    resistance = float(input("Enter resistance (Ω): "))
                    voltage = self.calc.ohms_law_voltage(current, resistance)
                    print(f"\nVoltage = {voltage} V")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "2":
                try:
                    voltage = float(input("Enter voltage (V): "))
                    resistance = float(input("Enter resistance (Ω): "))
                    current = self.calc.ohms_law_current(voltage, resistance)
                    print(f"\nCurrent = {current:.2f} A")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "3":
                try:
                    voltage = float(input("Enter voltage (V): "))
                    current = float(input("Enter current (A): "))
                    resistance = self.calc.ohms_law_resistance(voltage, current)
                    print(f"\nResistance = {resistance:.2f} Ω")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "4":
                try:
                    voltage = float(input("Enter voltage (V): "))
                    current = float(input("Enter current (A): "))
                    power = self.calc.power_calculation(voltage, current)
                    print(f"\nPower = {power} W")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "5":
                try:
                    resistances = []
                    n = int(input("Number of resistors: "))
                    for i in range(n):
                        r = float(input(f"Resistor {i+1} (Ω): "))
                        resistances.append(r)
                    total = self.calc.series_resistance(resistances)
                    print(f"\nTotal Series Resistance = {total} Ω")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "6":
                try:
                    resistances = []
                    n = int(input("Number of resistors: "))
                    for i in range(n):
                        r = float(input(f"Resistor {i+1} (Ω): "))
                        resistances.append(r)
                    total = self.calc.parallel_resistance(resistances)
                    print(f"\nTotal Parallel Resistance = {total:.2f} Ω")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "7":
                break
            
            else:
                print("Invalid option. Try again.")
    
    def handle_inventory(self):
        """Handle inventory menu"""
        while True:
            self.show_inventory_menu()
            choice = input("\nSelect option: ")
            
            if choice == "1":
                try:
                    eq_id = input("Equipment ID: ")
                    name = input("Equipment Name: ")
                    category = input("Category: ")
                    description = input("Description: ")
                    quantity = int(input("Quantity: "))
                    unit_cost = float(input("Unit Cost ($): "))
                    purchase_date = input("Purchase Date (YYYY-MM-DD): ")
                    
                    equipment = Equipment(eq_id, name, category, description, 
                                        quantity, unit_cost, purchase_date)
                    self.inventory.add_equipment(equipment)
                    print(f"\nEquipment '{name}' added successfully!")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "2":
                equipment_list = self.inventory.list_all_equipment()
                if not equipment_list:
                    print("\nNo equipment in inventory.")
                else:
                    print("\n--- Equipment List ---")
                    for eq in equipment_list:
                        print(f"{eq.name} (ID: {eq.equipment_id})")
                        print(f"  Quantity: {eq.quantity}")
                        print(f"  Status: {eq.status.value}")
                        print(f"  Total Value: ${eq.total_value():.2f}\n")
            
            elif choice == "3":
                try:
                    eq_id = input("Equipment ID: ")
                    new_quantity = int(input("New Quantity: "))
                    self.inventory.update_equipment_quantity(eq_id, new_quantity)
                    print(f"\nQuantity updated successfully!")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "4":
                try:
                    eq_id = input("Equipment ID: ")
                    print("\nStatus Options: available, in_use, maintenance, damaged, retired")
                    status_str = input("New Status: ").lower()
                    status = EquipmentStatus[status_str.upper()]
                    self.inventory.update_equipment_status(eq_id, status)
                    print(f"\nStatus updated successfully!")
                except (ValueError, KeyError) as e:
                    print(f"Error: Invalid status")
            
            elif choice == "5":
                total_value = self.inventory.get_total_inventory_value()
                print(f"\nTotal Inventory Value: ${total_value:.2f}")
            
            elif choice == "6":
                low_items = self.inventory.get_low_stock_items()
                if not low_items:
                    print("\nNo low stock items.")
                else:
                    print("\n--- Low Stock Items ---")
                    for item in low_items:
                        print(f"{item.name}: {item.quantity} units")
            
            elif choice == "7":
                break
            
            else:
                print("Invalid option. Try again.")
    
    def handle_circuit_simulation(self):
        """Handle circuit simulation"""
        while True:
            self.show_circuit_menu()
            choice = input("\nSelect option: ")
            
            if choice == "1":
                try:
                    circuit_id = input("Circuit ID: ")
                    name = input("Circuit Name: ")
                    description = input("Description: ")
                    circuit = Circuit(circuit_id, name, description)
                    self.circuits[circuit_id] = circuit
                    print(f"\nCircuit '{name}' created successfully!")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "2":
                if not self.circuits:
                    print("\nNo circuits created.")
                else:
                    print("\n--- Circuits ---")
                    for cid, circuit in self.circuits.items():
                        print(f"{circuit.name} (ID: {cid})")
                        print(f"  Components: {len(circuit.components)}\n")
            
            elif choice == "3":
                try:
                    circuit_id = input("Circuit ID: ")
                    if circuit_id not in self.circuits:
                        print("Circuit not found!")
                        continue
                    
                    circuit = self.circuits[circuit_id]
                    voltage = float(input("Supply Voltage (V): "))
                    circuit.set_power_source(voltage=voltage)
                    
                    # Add sample resistors if needed
                    if not circuit.components:
                        num_resistors = int(input("Number of resistors: "))
                        for i in range(num_resistors):
                            r_value = float(input(f"Resistor {i+1} value (Ω): "))
                            resistor = Component(f"R{i+1}", f"Resistor {i+1}", 
                                              ComponentType.RESISTOR, r_value, "Ω")
                            circuit.add_component(resistor)
                    
                    results = circuit.simulate_series_circuit()
                    print(f"\n--- Series Circuit Simulation ---")
                    print(f"Total Voltage: {results['total_voltage']} V")
                    print(f"Total Resistance: {results['total_resistance']} Ω")
                    print(f"Total Current: {results['total_current']:.2f} A")
                    print(f"Total Power: {results['total_power']:.2f} W")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "4":
                try:
                    circuit_id = input("Circuit ID: ")
                    if circuit_id not in self.circuits:
                        print("Circuit not found!")
                        continue
                    
                    circuit = self.circuits[circuit_id]
                    voltage = float(input("Supply Voltage (V): "))
                    circuit.set_power_source(voltage=voltage)
                    
                    # Add sample resistors if needed
                    if not circuit.components:
                        num_resistors = int(input("Number of resistors: "))
                        for i in range(num_resistors):
                            r_value = float(input(f"Resistor {i+1} value (Ω): "))
                            resistor = Component(f"R{i+1}", f"Resistor {i+1}", 
                                              ComponentType.RESISTOR, r_value, "Ω")
                            circuit.add_component(resistor)
                    
                    results = circuit.simulate_parallel_circuit()
                    print(f"\n--- Parallel Circuit Simulation ---")
                    print(f"Total Voltage: {results['total_voltage']} V")
                    print(f"Total Resistance: {results['total_resistance']:.2f} Ω")
                    print(f"Total Current: {results['total_current']:.2f} A")
                    print(f"Total Power: {results['total_power']:.2f} W")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "5":
                break
            
            else:
                print("Invalid option. Try again.")
    
    def handle_scheduling(self):
        """Handle workshop scheduling"""
        while True:
            self.show_scheduler_menu()
            choice = input("\nSelect option: ")
            
            if choice == "1":
                try:
                    session_id = input("Session ID: ")
                    title = input("Session Title: ")
                    description = input("Description: ")
                    instructor = input("Instructor Name: ")
                    start_time = input("Start Time (YYYY-MM-DD HH:MM:SS): ")
                    duration = float(input("Duration (hours): "))
                    max_participants = int(input("Max Participants: "))
                    
                    session = Session(session_id, title, description, instructor,
                                    start_time, duration, max_participants)
                    self.scheduler.add_session(session)
                    print(f"\nSession '{title}' created successfully!")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "2":
                sessions = self.scheduler.list_all_sessions()
                if not sessions:
                    print("\nNo sessions scheduled.")
                else:
                    print("\n--- Scheduled Sessions ---")
                    for session in sessions:
                        print(f"{session.title}")
                        print(f"  Instructor: {session.instructor}")
                        print(f"  Participants: {len(session.participants)}/{session.max_participants}\n")
            
            elif choice == "3":
                try:
                    session_id = input("Session ID: ")
                    participant_name = input("Participant Name: ")
                    self.scheduler.register_participant(session_id, participant_name)
                    print(f"\n{participant_name} registered successfully!")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "4":
                try:
                    session_id = input("Session ID: ")
                    session = self.scheduler.get_session(session_id)
                    print(f"\n--- Session Details ---")
                    print(f"Title: {session.title}")
                    print(f"Instructor: {session.instructor}")
                    print(f"Start Time: {session.start_time}")
                    print(f"Duration: {session.duration_hours} hours")
                    print(f"Participants: {len(session.participants)}/{session.max_participants}")
                    print(f"Status: {session.status.value}")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "5":
                upcoming = self.scheduler.get_upcoming_sessions()
                if not upcoming:
                    print("\nNo upcoming sessions.")
                else:
                    print("\n--- Upcoming Sessions ---")
                    for session in upcoming:
                        print(f"{session.title} - {session.start_time}")
            
            elif choice == "6":
                break
            
            else:
                print("Invalid option. Try again.")
    
    def handle_documentation(self):
        """Handle documentation system"""
        while True:
            self.show_documentation_menu()
            choice = input("\nSelect option: ")
            
            if choice == "1":
                try:
                    doc_id = input("Document ID: ")
                    title = input("Document Title: ")
                    print("\nDocument Types: technical_specification, assembly_guide, "
                          "circuit_diagram, troubleshooting_guide, maintenance_guide")
                    doc_type = input("Document Type: ")
                    author = input("Author: ")
                    content = input("Document Content: ")
                    
                    document = TechnicalDocument(doc_id, title, doc_type, author, content)
                    self.documentation.add_document(document)
                    print(f"\nDocument '{title}' created successfully!")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "2":
                documents = self.documentation.list_all_documents()
                if not documents:
                    print("\nNo documents in repository.")
                else:
                    print("\n--- Documents ---")
                    for doc in documents:
                        print(f"{doc.title} (ID: {doc.doc_id})")
                        print(f"  Type: {doc.doc_type}")
                        print(f"  Author: {doc.author}\n")
            
            elif choice == "3":
                keyword = input("Search keyword: ")
                results = self.documentation.search_by_title(keyword)
                if not results:
                    print("\nNo documents found.")
                else:
                    print("\n--- Search Results ---")
                    for doc in results:
                        print(f"{doc.title} (ID: {doc.doc_id})")
            
            elif choice == "4":
                stats = self.documentation.get_document_statistics()
                print(f"\n--- Documentation Statistics ---")
                print(f"Total Documents: {stats['total_documents']}")
                print(f"By Type: {stats['by_type']}")
                print(f"Total Authors: {stats['total_authors']}")
            
            elif choice == "5":
                try:
                    doc_id = input("Document ID: ")
                    document = self.documentation.get_document(doc_id)
                    print("\n" + document.to_markdown())
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "6":
                break
            
            else:
                print("Invalid option. Try again.")
    
    def show_system_info(self):
        """Show system information"""
        print("\n--- System Information ---")
        print(f"Equipment in Inventory: {len(self.inventory.list_all_equipment())}")
        print(f"Circuits Created: {len(self.circuits)}")
        print(f"Scheduled Sessions: {len(self.scheduler.list_all_sessions())}")
        print(f"Documents: {self.documentation.get_document_statistics()['total_documents']}")
    
    def run(self):
        """Run the application"""
        print("\nWelcome to Electrical Workshop Management System!")
        
        while self.is_running:
            self.display_menu()
            choice = input("\nSelect option: ")
            
            if choice == "1":
                self.handle_calculations()
            elif choice == "2":
                self.handle_inventory()
            elif choice == "3":
                self.handle_circuit_simulation()
            elif choice == "4":
                self.handle_scheduling()
            elif choice == "5":
                self.handle_documentation()
            elif choice == "6":
                self.show_system_info()
            elif choice == "0":
                print("\nThank you for using Electrical Workshop Management System!")
                self.is_running = False
            else:
                print("Invalid option. Try again.")


if __name__ == "__main__":
    app = WorkshopManagementSystem()
    app.run()
