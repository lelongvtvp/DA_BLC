// Địa chỉ contract đã deploy
const contractAddress = "0x02f9Be4AC6457912d275B4f576537466ad958D42"; 

// Tải ABI từ file JSON
fetch("abi.js")
  .then(res => res.json())
  .then(async abi => {
    // Kết nối với MetaMask
    if (!window.ethereum) return alert("Vui lòng cài MetaMask!");

    await window.ethereum.request({ method: "eth_requestAccounts" });

    const provider = new ethers.BrowserProvider(window.ethereum);
    const signer = await provider.getSigner();
    const contract = new ethers.Contract(contractAddress, abi, signer);

    // Hiển thị thông điệp hiện tại
    async function loadMessage() {
      const message = await contract.getMessage();
      document.getElementById("currentMessage").innerText = message;
    }

    window.updateMessage = async function () {
      const newMsg = document.getElementById("newMessage").value;
      const tx = await contract.updateMessage(newMsg);
      await tx.wait();
      loadMessage();
    }

    loadMessage();
  });
