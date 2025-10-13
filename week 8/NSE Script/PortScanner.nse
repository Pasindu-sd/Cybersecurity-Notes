description = [[My first NSE Script for port scanner]]
author = "Pasindu Sandeepa Dilhara"
license = "Same as Nmap"

categories = {"safe", "discovery"}

portrule = function(host, port)
  return port.state == "open"
end

action = function(host, port)
  local result = string.format("Port %d/%s is OPEN", port.number, port.protocol)
end
