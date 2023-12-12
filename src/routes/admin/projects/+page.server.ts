import type { PageServerLoad } from './$types';
import { SERVEUR_URL } from '$env/static/private'

export const load: PageServerLoad = () => {
    const projects = fetch(`${SERVEUR_URL}/api/projects/`).then(res => res.json())
    return {
        projects
    }
}