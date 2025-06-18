export async function getAgentData() {
    const response = await fetch('/api/agent');
    return response.json();
}
