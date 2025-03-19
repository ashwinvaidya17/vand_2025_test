async function loadResults() {
    try {
        // Fetch the CSV file
        const response = await fetch('results.csv');
        const csvText = await response.text();

        // Parse CSV (skip header row)
        const rows = csvText.split('\n')
            .slice(1)  // Skip header
            .filter(row => row.trim() !== '')  // Remove empty rows
            .map(row => {
                const [pr_name, pr_number, commit_sha, timestamp, score, pr_actor] = row.split(',');
                return {
                    pr_name: pr_name,
                    pr_number: parseInt(pr_number),
                    commit_sha: commit_sha,
                    timestamp: new Date(timestamp),
                    score: parseFloat(score),
                    pr_actor: pr_actor
                };
            });

        // Sort by score (highest first)
        rows.sort((a, b) => b.score - a.score);

        // Create table HTML
        const table = `
            <table>
                <thead>
                    <tr>
                        <th>Rank</th>
                        <th>PR #</th>
                        <th>Score</th>
                        <th>Timestamp</th>
                        <th>Commit</th>
                    </tr>
                </thead>
                <tbody>
                    ${rows.map((row, index) => `
                        <tr>
                            <td>${index + 1}</td>
                            <td><a href="TODO">#${row.pr_number}</a></td>
                            <td>${row.score.toFixed(4)}</td>
                            <td>${row.timestamp.toLocaleString()}</td>
                            <td><a href="TODO">${row.commit_sha.slice(0, 7)}</a></td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        `;

        // Add table to content div
        document.getElementById('content').innerHTML = table;
    } catch (error) {
        console.error('Error loading results:', error);
        document.getElementById('content').innerHTML = '<p>Error loading results. Please try again later.</p>';
    }
}

// Load results when page loads
document.addEventListener('DOMContentLoaded', loadResults);
