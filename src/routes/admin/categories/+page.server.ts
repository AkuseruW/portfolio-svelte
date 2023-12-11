import type { PageServerLoad } from './$types';
import { SERVEUR_URL } from '$env/static/private'


export const load: PageServerLoad = () => {
    return {
        categories: fetch(`${SERVEUR_URL}/api/categories/`).then(res => res.json())
    }
}