#include <iostream>
#include <vector>
#include <string>
#include <boost/asio.hpp>

using namespace boost::asio;

int main() {
    // --- Portfolio setup ---
    double cash = 10000.0; // USD
    double eth = 0.0;      // ETH

    // --- Simulated price feed ---
    std::vector<double> prices = {1850.5, 1860.2, 1855.0, 1870.3, 1865.5, 1875.0};

    // --- Serial port setup ---
    io_service io;
    serial_port port(io, "/dev/ttyUSB0"); // change to your port
    port.set_option(serial_port_base::baud_rate(9600));
    port.set_option(serial_port_base::character_size(8));
    port.set_option(serial_port_base::parity(serial_port_base::parity::none));
    port.set_option(serial_port_base::stop_bits(serial_port_base::stop_bits::one));
    port.set_option(serial_port_base::flow_control(serial_port_base::flow_control::none));

    std::cout << "Starting ETHUSD trade simulation...\n";

    for (size_t i = 0; i < prices.size(); ++i) {
        double price = prices[i];
        char signal;

        // --- Read UART signal ---
        read(port, buffer(&signal, 1));

        switch(signal) {
            case 'B':
            case 'b':
                if (cash >= price) {
                    double amount = cash / price;  // buy max ETH
                    eth += amount;
                    cash -= amount * price;
                    std::cout << "Bought " << amount << " ETH at $" << price << "\n";
                } else {
                    std::cout << "Not enough cash to buy.\n";
                }
                break;

            case 'S':
            case 's':
                if (eth > 0) {
                    cash += eth * price;
                    std::cout << "Sold " << eth << " ETH at $" << price << "\n";
                    eth = 0;
                } else {
                    std::cout << "No ETH to sell.\n";
                }
                break;

            case 'H':
            case 'h':
                std::cout << "Holding. No trade executed.\n";
                break;

            default:
                std::cout << "Invalid UART signal: " << signal << "\n";
                break;
        }

        std::cout << "Portfolio -> Cash: $" << cash << ", ETH: " << eth
                  << " (Value: $" << eth*price << ")\n\n";
    }

    double final_value = cash + eth * prices.back();
    std::cout << "Simulation complete. Final portfolio value: $" << final_value << "\n";

    return 0;
}
