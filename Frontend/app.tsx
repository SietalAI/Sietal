import React from 'react';
import WalletConnector from './WalletConnector';
import AgentSettingsPanel from './AgentSettingsPanel';
import RewardsDashboard from './RewardsDashboard';

function App() {
    return (
        <div>
            <WalletConnector />
            <AgentSettingsPanel />
            <RewardsDashboard />
        </div>
    );
}

export default App;
