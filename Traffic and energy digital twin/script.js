const trafficDensityElement = document.getElementById("trafficDensity");
const energyConsumptionElement = document.getElementById("energyConsumption");
function getRandomData() {
    const trafficDensity = Math.floor(Math.random() * 100); 
    const energyConsumption = (Math.random() * 500).toFixed(2); 
    return { trafficDensity, energyConsumption };
}
function updateData() {
    const data = getRandomData();
    trafficDensityElement.textContent = `${data.trafficDensity} %`;
    energyConsumptionElement.textContent = `${data.energyConsumption} MW`;
}
document.getElementById("refreshButton").addEventListener("click", updateData);
updateData();
