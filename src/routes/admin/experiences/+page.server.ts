import type { PageServerLoad } from './$types';
import { SERVEUR_URL } from '$env/static/private'

export const load: PageServerLoad = () => {
    const experiences = fetch(`${SERVEUR_URL}/api/experiences/`).then(res => res.json())
    return {
        experiences
    }
}

