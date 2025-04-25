const hre = require("hardhat");

async function main() {
  const MessageBoard = await hre.ethers.getContractFactory("MessageBoard");
  const messageBoard = await MessageBoard.deploy("Chào Blockchain!");

  // 🔧 Đảm bảo bạn await đúng object trước khi dùng .deployed()
  await messageBoard.waitForDeployment();

  console.log(`✅ MessageBoard deployed at: ${messageBoard.target}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
