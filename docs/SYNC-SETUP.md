# Setting up sync for your copy of Lineage Tracker

Sync goes through each person's own cloud storage. Whoever hosts a copy of Lineage Tracker adds one or both keys to `config.json` next to `index.html`.

## Dropbox

1. Go to https://www.dropbox.com/developers/apps and choose **Create app**.
2. Choose **Scoped access**, then **App folder**, and give it a name, such as "Lineage Tracker Sync".
3. On the **Permissions** tab, tick `files.content.write`, `files.content.read` and `files.metadata.read`, then **Submit**.
4. On the **Settings** tab, under **OAuth 2**:
   - add the app's address as a **Redirect URI**, exactly: `https://app.lineagetracker.org/`
   - set **Allow public clients (Implicit Grant & PKCE)** to **Allow**.
5. Copy the **App key** (not the secret) into `config.json`:

```
{
  "siteUrl": "https://app.lineagetracker.org/",
  "dropboxAppKey": "PASTE-THE-APP-KEY"
}
```

New Dropbox apps start in development status, which limits how many people can connect before you apply for production status in the same console.

## Google Drive

Needs a Google Cloud project with an OAuth client ID for a web application, the Drive API enabled, and `https://app.lineagetracker.org` as an authorised JavaScript origin. Add it as `"googleClientId"` in `config.json`.
