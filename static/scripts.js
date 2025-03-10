async function fetchBlockchain() {
    try {
        const response = await fetch('/chain');

        if (!response.ok) {
            throw new Error(`Lỗi HTTP: ${response.status}`);
        }

        const data = await response.json();
        document.getElementById('blockchainData').innerHTML = 
            `<pre>${JSON.stringify(data.chain, null, 4)}</pre>`;
    } catch (error) {
        console.error("Lỗi khi lấy blockchain:", error);
        document.getElementById('blockchainData').textContent = "Không thể tải blockchain!";
    }
}
async function sendTransaction() {
    const sender = document.getElementById('sender').value.trim();
    const receiver = document.getElementById('receiver').value.trim();
    const amount = parseFloat(document.getElementById('amount').value);

    if (!sender || !receiver || isNaN(amount) || amount <= 0) {
        alert("Vui lòng nhập thông tin hợp lệ!");
        return;
    }

    try {
        const response = await fetch('/transactions/new', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ sender, receiver, amount })
        });

        if (response.ok) {
            alert("Giao dịch đã được gửi!");
            fetchBlockchain();  // Cập nhật blockchain sau khi giao dịch
        } else {
            alert("Giao dịch thất bại!");
        }
    } catch (error) {
        console.error("Lỗi khi gửi giao dịch:", error);
        alert("Có lỗi xảy ra, vui lòng thử lại!");
    }
}

async function mineBlock() {
    try {
        const response = await fetch('/mine');
        if (response.ok) {
            alert("Block đã được đào thành công!");
            fetchBlockchain();  // Cập nhật blockchain sau khi đào block
        } else {
            alert("Lỗi khi đào block!");
        }
    } catch (error) {
        console.error("Lỗi khi đào block:", error);
        alert("Có lỗi xảy ra khi đào block!");
    }
}

// Tải blockchain khi mở trang
document.addEventListener("DOMContentLoaded", fetchBlockchain);
