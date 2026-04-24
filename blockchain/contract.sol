// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LogIntegrity {

    struct LogRecord {
        string hash;
        uint256 timestamp;
        address sender;
    }

    LogRecord[] private records;

    event HashStored(
        uint256 indexed index,
        string hash,
        uint256 timestamp,
        address sender
    );

    // 🔐 Store log hash
    function storeHash(string memory _hash) public {
        records.push(LogRecord({
            hash: _hash,
            timestamp: block.timestamp,
            sender: msg.sender
        }));

        emit HashStored(
            records.length - 1,
            _hash,
            block.timestamp,
            msg.sender
        );
    }

    // 🔍 Get hash by index
    function getHash(uint256 index) public view returns (string memory) {
        require(index < records.length, "Invalid index");
        return records[index].hash;
    }

    // 📊 Get total logs stored
    function getCount() public view returns (uint256) {
        return records.length;
    }

    // 📦 Get full record (for advanced demo)
    function getRecord(uint256 index) public view returns (
        string memory,
        uint256,
        address
    ) {
        require(index < records.length, "Invalid index");

        LogRecord memory record = records[index];
        return (record.hash, record.timestamp, record.sender);
    }
}