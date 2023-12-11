import type { PageServerLoad } from './$types';
import { SERVEUR_URL } from '$env/static/private'

export const load: PageServerLoad = () => {
    return {
        skills: fetch(`${SERVEUR_URL}/api/skills/`).then(res => res.json())
    }
}