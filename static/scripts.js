async function fetchBlockchain() {
    const response = await fetch('/chain');
    const data = await response.json();
    document.getElementById('blockchainData').textContent = JSON.stringify(data.chain, null, 2)
}

async function senTransaction() {
    const sender = document.getElementById('sender').value;
    const receiver = document.getElementById('receiver').value;
    const amount = document.getElementById('amount').value;

    const response = await fetch('/transactions/new', {
        method: 'POST', 
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({sender, receiver, amount})
    });

    alert("Giao dịch đã được gửi!")

}

async function mineBlock() {
    const response = await fetch('/mine');
    const data = await response.json();
    alert("Block đã được đào");
    fetchBlockchain();
}
