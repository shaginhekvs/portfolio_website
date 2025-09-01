# Portfolio Website (Flask) — Make It Yours & Deploy on Render


Create a clean personal portfolio in minutes. Find example at https://www.keshavsingh.site/ .
Edit your details in `app.py`, run locally, and deploy to the web with **Render** in a few clicks.

---

## What’s inside

```
.
├── app.py                 # Flask app — edit this with your CV details
├── templates/             # Jinja HTML templates
├── static/                # CSS / JS / images
└── requirements.txt       # Python dependencies
```

> The repo contains a Flask app with `templates/` and `static/` assets, plus `requirements.txt`. ([GitHub][1])

---

## Quick start (local)

1. Clone:

```bash
git clone https://github.com/shaginhekvs/portfolio_website.git
cd portfolio_website
```

2. Create & activate a virtual env:

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

3. Install deps:

```bash
pip install -r requirements.txt
```

4. Run the app (choose one):

**A. Flask CLI**

```bash
export FLASK_APP=app.py        # Windows: set FLASK_APP=app.py
flask run
```

**B. Python directly**

```bash
python app.py
```

---

## Make it yours (edit `app.py`)

Open `app.py` and replace the placeholder fields with your own details:

* Name, Title, Location
* Short bio / About
* Skills & tools
* Work experience & education
* Selected projects (title, description, links)
* Social links (GitHub, LinkedIn, X, etc.)

Save and refresh — your content renders through the Jinja templates.

---

## One-click style changes

Edit the files in `templates/` and `static/` to tweak layout, colors, and images. Keep the route names in `app.py` the same unless you also update the template links.

---

## Deploy to the web (Render)

You can deploy a Flask app on **Render** quickly; Render expects your web service to bind to host **`0.0.0.0`** and the port provided via the **`PORT`** environment variable. ([Render][2])

### Steps

1. **Push to GitHub** (this repo or your fork).
2. **Create a Render account**, click **New → Web Service**, and **Connect** your repository. ([Render][3])
3. **Environment:** *Python*
4. **Build Command:**

   ```bash
   pip install -r requirements.txt
   ```
5. **Start Command (Gunicorn):**

   ```bash
   gunicorn app:app --bind 0.0.0.0:$PORT
   ```

   * `gunicorn` is the recommended WSGI server for Flask in production. If `PORT` is defined, Gunicorn defaults to `0.0.0.0:$PORT`, but binding explicitly avoids confusion on some platforms. ([flask.palletsprojects.com][4], [docs.gunicorn.org][5])
6. Click **Create Web Service** and wait for the deploy to finish. That’s it. ([Render][2])

> Tip: If you see “no open ports detected,” double-check that you’re binding to `0.0.0.0:$PORT` and that `gunicorn` is listed in `requirements.txt`. ([Render][6])

---

## Common tweaks

* **Custom domain:** Add it from your Render service settings after the first successful deploy. ([Render][3])
* **Environment variables:** Use Render → *Environment* to store secrets (e.g., analytics keys). ([Teclado REST APIs][7])

---

## FAQ

**Do I have to use Render?**
No—any host that supports Python + WSGI (Gunicorn) works. The key is to bind to `0.0.0.0` and the correct port for your provider. ([flask.palletsprojects.com][4])

**How do I change the layout?**
Edit the HTML in `templates/` and the styles in `static/`. Keep Jinja placeholders intact unless you update `app.py` accordingly.

---

## License

If you plan to share or modify this project, consider adding a license file (e.g., MIT) at the repo root.

---

## Credits

Built with **Flask**, **Jinja**, and **Gunicorn**. Deployment instructions adapted from Render’s docs. ([Render][2])

---

Happy shipping! 🎉

[1]: https://github.com/shaginhekvs/portfolio_website "GitHub - shaginhekvs/portfolio_website"
[2]: https://render.com/docs/deploy-flask "Deploy a Flask App on Render"
[3]: https://render.com/docs/your-first-deploy "Your First Render Deploy"
[4]: https://flask.palletsprojects.com/en/stable/deploying/gunicorn/ "Gunicorn — Flask Documentation (3.1.x)"
[5]: https://docs.gunicorn.org/en/stable/settings.html "Settings — Gunicorn 23.0.0 documentation"
[6]: https://community.render.com/t/why-cant-reach-my-website-despite-the-service-being-live/17839 "Why can't reach my website despite the service being live"
[7]: https://rest-apis-flask.teclado.com/docs/deploy_to_render/environment_variables_and_migrations/ "How to use Environment Variables in Render.com"
