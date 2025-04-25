require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.28",
};
module.exports = {
  solidity: "0.8.28",
  networks: {
    ganache: {
      url: "http://127.0.0.1:7545",
      accounts: [
        "0xa56f857ec6c6edd7210f973e3ff7240f0e6e8536a5d28141c5a84d7436cd33f8"
      ]
    }
  }
};