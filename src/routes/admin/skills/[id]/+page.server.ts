import type { PageServerLoad, Actions } from './$types';
import { SERVEUR_URL } from '$env/static/private'
import { error } from '@sveltejs/kit';


export const load: PageServerLoad = async ({ params }) => {
    const skill = await fetch(`${SERVEUR_URL}/api/skills/${params.id}`).then(res => res.json())
    const categories = await fetch(`${SERVEUR_URL}/api/categories/`).then(res => res.json())

    if (skill) {
        return {
            skill,
            categories
        }
    }

    throw error(404, 'Category not found');
}


export const actions: Actions = {
    update_skill: async ({ request }) => {
        const formData = await request.formData();

        if (!formData.get('name')) {
            return {
                error: 'Name is required'
            }
        }

        const res = await fetch(`${SERVEUR_URL}/api/skills/${formData.get('id')}`, {
            method: 'PATCH',
            body: formData,
        })

        if (res.ok) {
            return { success: true };
        } else {
            return {
                error: 'Failed to update category'
            }
        }
    }

}