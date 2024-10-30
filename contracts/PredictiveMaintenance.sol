// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PredictiveMaintenance {
    struct MaintenanceLog {
        uint id;
        string ipfsHash;
        string dataHash;
        bool maintenanceNeeded;
        uint timestamp;
    }

    MaintenanceLog[] public logs;
    uint public logCount;

    event MaintenanceLogged(uint id, string ipfsHash, string dataHash, bool maintenanceNeeded, uint timestamp);

    function logMaintenance(string memory _ipfsHash, string memory _dataHash, bool _maintenanceNeeded) public {
        logCount++;
        logs.push(MaintenanceLog(logCount, _ipfsHash, _dataHash, _maintenanceNeeded, block.timestamp));
        emit MaintenanceLogged(logCount, _ipfsHash, _dataHash, _maintenanceNeeded, block.timestamp);
    }

    function getMaintenanceLog(uint _id) public view returns (MaintenanceLog memory) {
        require(_id > 0 && _id <= logCount, "Log does not exist");
        return logs[_id - 1];
    }
}
